from datetime import datetime
import re
from connector import es_connect

es = es_connect() # connecting to Elasticsearch


def es_search():
    today = datetime.strftime(datetime.now(), 'filebeat-%Y.%m.%d')  # format index for today
    res = es.search(index=today, body={'query': {'match': {'message': 'Failed password'}}})
    # res = es.search(index=today, body={'query': {'match': {'message': 'dfsdfsdfsdfsdfsdfsdfsdf'}}})   # testing empty result
    # print('{} documents found'.format(res['hits']['total']))  # how many documents found
    # print(res['hits']['hits'])

    regex_ip = re.compile(r'([0-9]{1,3}\.){3}[0-9]{1,3}')   # regex for find IPv4

    ip_who_attack = {}  # dict for founded ip addresses
    if res['hits']['total'] > 0:
        for doc in res['hits']['hits']:
            if 'sshd' in doc['_source']['message']:
                ip = regex_ip.search(doc['_source']['message']).group()
                if ip in ip_who_attack:
                    ip_who_attack.update({ip: ip_who_attack[ip] + 1})
                else:
                    ip_who_attack.update({ip: 1})
            else:
                #print('Today there was no attack on ssh.')
                return False    # there are no 'sshd' in log
    else:
        print('Today there was no attack on ssh.')
        return False    # no search result
    return ip_who_attack
    # print(ip, doc['_source']['@timestamp'])
    # print("At Host {} --- {}".format(doc['_source']['beat']['hostname'], doc['_source']['message']))
