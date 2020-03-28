import numpy as np


def init_q(s, a, type="zeros"):
    """
    @param s the number of states
    @param a the number of actions
    @param type random, ones or zeros for the initialization
    """
    if type == "ones":
        return np.ones((s, a))
    elif type == "random":
        return np.random.random((s, a))
    elif type == "zeros":
        return np.zeros((s, a))

def epsilon_greedy(Q, epsilon, n_actions, s, train=False):
    """
    @param Q Q values state x action -> value
    @param epsilon for exploration
    @param s number of states
    @param train if true then no random actions selected
    """
    if train or np.random.rand() < epsilon: #rand() random flotante 0-1
        action = np.argmax(Q[s, :])
    else:
        action = np.random.randint(0, n_actions)
    return action


class Qagent:
    def __init__(self, alpha, gamma, epsilon, episodes, n_states, n_actions):

        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.episodes = episodes
        self.n_actions = n_actions
        self.n_states = n_states
        self.Q = init_q(n_states, n_actions, type="ones")

    def take_action(self,s,first_state):
        if first_state:
            action = epsilon_greedy(self.Q,self.epsilon,self.n_actions,s,False)
        else:
            s_=s
            action = np.argmax(self.Q[s_, :])
        return action

    def updateQ(self,reward,s,a,s_,a_,end_sate):
        Q=self.Q
        alpha = self.alpha
        gamma = self.gamma
    
        if end_sate:
            print("*** Terminal state")
            Q[s, a] += alpha * (reward - Q[s, a])

        else:
            Q[s, a] += alpha * (reward + (gamma * Q[s_, a_]) - Q[s, a])


