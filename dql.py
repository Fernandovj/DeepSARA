
import numpy as np
import tensorflow as tf
import collections as cns


def dense(x, weights, bias, activation=tf.identity, **activation_kwargs):
    """Dense layer."""
    #x = x.astype("float32")
    #print("##x",x)
    #print("##weights",weights)
    z = tf.matmul(x, weights) + bias
    return activation(z, **activation_kwargs)


def init_weights(shape, initializer):
    """Initialize weights for tensorflow layer."""
    weights = tf.Variable(
        initializer(shape),
        trainable=True,
        dtype=tf.float32
    )

    return weights


class Network(object):
    """Q-function approximator."""

    def __init__(self,
                 input_size,
                 output_size,
                 hidden_size=[50, 50],
                 weights_initializer=tf.initializers.glorot_uniform(),
                 bias_initializer=tf.initializers.zeros(),
                 optimizer=tf.optimizers.Adam,
                 **optimizer_kwargs):
        """Initialize weights and hyperparameters."""
        self.input_size = input_size
        self.output_size = output_size
        self.hidden_size = hidden_size

        np.random.seed(41)

        self.initialize_weights(weights_initializer, bias_initializer)
        self.optimizer = optimizer(**optimizer_kwargs)

    def initialize_weights(self, weights_initializer, bias_initializer):
        """Initialize and store weights."""
        wshapes = [
            [self.input_size, self.hidden_size[0]],
            [self.hidden_size[0], self.hidden_size[1]],
            [self.hidden_size[1], self.output_size]
        ]

        bshapes = [
            [1, self.hidden_size[0]],
            [1, self.hidden_size[1]],
            [1, self.output_size]
        ]

        self.weights = [init_weights(s, weights_initializer) for s in wshapes]
        self.biases = [init_weights(s, bias_initializer) for s in bshapes]

        self.trainable_variables = self.weights + self.biases

    def model(self, inputs):
        """Given a state vector, return the Q values of actions."""
        h1 = dense(inputs, self.weights[0], self.biases[0], tf.nn.relu) #hidden layer 1
        h2 = dense(h1, self.weights[1], self.biases[1], tf.nn.relu) #hidden layer 2

        out = dense(h2, self.weights[2], self.biases[2])

        return out

    def train_step(self, inputs, targets, actions_one_hot):
        """Update weights."""
        with tf.GradientTape() as tape:
            qvalues = tf.squeeze(self.model(inputs))
            preds = tf.reduce_sum(qvalues * actions_one_hot, axis=1)
            loss = tf.losses.mean_squared_error(targets, preds)

        grads = tape.gradient(loss, self.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.trainable_variables)) #gradient descent


class Memory(object):
    """Memory buffer for Experience Replay."""

    def __init__(self, max_size):
        """Initialize a buffer containing max_size experiences."""
        self.buffer = cns.deque(maxlen=max_size)

    def add(self, experience):
        """Add an experience to the buffer."""
        self.buffer.append(experience)

    def sample(self, batch_size):
        """Sample a batch of experiences from the buffer."""
        buffer_size = len(self.buffer)
        print("**",buffer_size)
        index = np.random.choice(np.arange(buffer_size), size=batch_size, replace=False)
        return [self.buffer[i] for i in index]

    def __len__(self):
        """Interface to access buffer length."""
        return len(self.buffer)


class Agent(object):
    """Deep Q-learning agent."""

    def __init__(self,
                 state_space_size,
                 action_space_size,
                 target_update_freq=100, #1000, #cada n steps se actualiza la target network
                 discount=0.99,
                 batch_size=32,
                 max_explore=1,
                 min_explore=0.05,
                 anneal_rate=(1/5000), #100000),
                 replay_memory_size=100000,
                 replay_start_size= 500): #500): #10000): #despues de n steps comienza el replay
        """Set parameters, initialize network."""
        self.action_space_size = action_space_size

        self.online_network = Network(state_space_size, action_space_size)
        self.target_network = Network(state_space_size, action_space_size)

        self.update_target_network()

        # training parameters
        self.target_update_freq = target_update_freq
        self.discount = discount
        self.batch_size = batch_size

        # policy during learning
        self.max_explore = max_explore + (anneal_rate * replay_start_size)
        self.min_explore = min_explore
        self.anneal_rate = anneal_rate
        self.steps = 0

        # replay memory
        self.memory = Memory(replay_memory_size)
        self.replay_start_size = replay_start_size
        self.experience_replay = Memory(replay_memory_size)

    def handle_episode_start(self):
        self.last_state, self.last_action = None, None

    def step(self, state, reward, training=True):
        """Observe state and rewards, select action.
        It is assumed that `observation` will be an object with
        a `state` vector and a `reward` float or integer. The reward
        corresponds to the action taken in the previous step.
        """
        last_state, last_action = self.last_state, self.last_action
        last_reward = reward
        state = state
        
        action = self.policy(state, training)

        if training:
            self.steps += 1
            print("## step:",self.steps)

            if last_state is not None:
                experience = {
                    "state": last_state,
                    "action": last_action,
                    "reward": last_reward,
                    "next_state": state
                }

                self.memory.add(experience)
                #print("**memory size:",self.memory.__len__())
            #else:
                #print("&& last_state",last_state)

            if self.steps > self.replay_start_size: #para acumular cierta cantidad de experiences antes de comenzar el entrenamiento
                self.train_network()

                if self.steps % self.target_update_freq == 0: #el clon de la red se realiza cada cierta cant de steps
                    self.update_target_network()

        self.last_state = state
        self.last_action = action

        return action

    def policy(self, state, training):
        """Epsilon-greedy policy for training, greedy policy otherwise."""
        explore_prob = self.max_explore - (self.steps * self.anneal_rate)#probabilidad de exploracion decreciente
        explore = max(explore_prob, self.min_explore) > np.random.rand()

        if training and explore: #hacer exploracion
            action = np.random.randint(self.action_space_size)
        else: #hacer explotacion
            inputs = np.expand_dims(state, 0)
            qvalues = self.online_network.model(inputs) #online or evalation network predicts q-values
            #print("***##qvalues",qvalues)
            action = np.squeeze(np.argmax(qvalues, axis=-1))

        return action

    def update_target_network(self):
        """Update target network weights with current online network values."""
        variables = self.online_network.trainable_variables
        variables_copy = [tf.Variable(v) for v in variables]
        self.target_network.trainable_variables = variables_copy

    def train_network(self):
        """Update online network weights."""
        batch = self.memory.sample(self.batch_size)
        inputs = np.array([b["state"] for b in batch]) #####
        actions = np.array([b["action"] for b in batch])
        rewards = np.array([b["reward"] for b in batch])
        next_inputs = np.array([b["next_state"] for b in batch])

        actions_one_hot = np.eye(self.action_space_size)[actions]

        next_qvalues = np.squeeze(self.target_network.model(next_inputs))
        targets = rewards + self.discount * np.amax(next_qvalues, axis=-1)

        self.online_network.train_step(inputs, targets, actions_one_hot)
