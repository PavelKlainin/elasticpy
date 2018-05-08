from es_search import es_search
from send_message import telegram


ip = es_search()
print(ip)
message = 'Banned IP: {}'.format(ip)

telegram(message)

