import requests

token = "802783389:AAGG3pR2VA5e3caRXTfFTqt6aU5cWk1i5FM" 
url="https://api.telegram.org/bot"+token+"/sendMessage"

def sendMessage(message):
    #'chat_id': '787248960' Dani
    
    data = {
        'chat_id': '835968219',  
        'text': message
    }

    response = requests.post(url, data=data)
    print(response)