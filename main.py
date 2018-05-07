from elasticsearch import Elasticsearch
import sys
from datetime import datetime
import re


try:
    es = Elasticsearch([{'host': '192.168.7.5', 'port': 9200}])
    print('Connected', es.info())
except Exception as ex:
    print('Error: ', ex)
    sys.exit()


#def es_query:


today = datetime.strftime(datetime.now(), 'filebeat-%Y.%m.%d')

res = es.search(index=today, body={'query': {'prefix': {'message': 'sshd'}}})

#res = es.search(index=today, body={'query': {'prefix': )

print('{} documents found'.format(res['hits']['total']))
#print(res['hits']['hits'])

regex_ip = re.compile(r'([0-9]{1,3}\.){3}[0-9]{1,3}')

for doc in res['hits']['hits']:
    if 'Failed' in doc['_source']['message']:
        ip = regex_ip.search(doc['_source']['message']).group()
        print(ip)
        #print("At Host {} --- {}".format(doc['_source']['beat']['hostname'], doc['_source']['message']))
        #if regex_ip in

