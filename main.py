from es_search import es_search
from send_message import telegram
import subprocess

if es_search():
    ip_dict = es_search()
    for ip, quantity in ip_dict.items():
        if quantity >= 4:
            message = 'From IP {} server was attacked {} times. Banish him!'.format(ip, quantity)
            cmd = 'iptables -A INPUT -s {} -p tcp --dport 22 -j DROP'.format(ip)
            telegram(message)
            print(message + '\n' + cmd)
            subprocess.call(cmd, shell=True)


