import requests


def telegram(message_text):
    url = 'https://api.telegram.org/bot'
    token = '570654445:AAEuG6C3cdKuPMdBJ0FYtdFI11bYw-3BoDQ'
    chat_id = '535079184'
    message_data = {'chat_id': chat_id, 'text': message_text, 'parse_mode': 'HTML'}

    try:
        requests.post(url + token + '/sendMessage', data=message_data)

    except:
        print('Send message error')
        return False
