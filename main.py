from es_search import es_search
from send_message import telegram
import subprocess

if es_search():
    ip_dict = es_search()
    print(ip_dict)
    for ip, quantity in ip_dict.items():
        if quantity >= 4:
            cmd = 'echo iptables -A INPUT -s {} -p tcp --dport 22 -j DROP'.format(ip)
            print(cmd)
            #subprocess.call(cmd)



    message = 'Banned IP: {}'.format(ip)

    telegram(message)

