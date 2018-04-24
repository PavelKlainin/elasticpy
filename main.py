from elasticsearch import Elasticsearch
#import datetime
from datetime import datetime

es = Elasticsearch([{'host': '192.168.7.5', 'port': 9200}])

#def es_query:
#print(es.info())
#print(datetime.datetime.now())

today = datetime.strftime(datetime.now(), 'filebeat-%Y.%m.%d')
#print(today)

res = es.search(index=today, body={"query": {"prefix": {"message": "sshd"}}})

print("{} documents found".format(res['hits']['total']))

for doc in res['hits']['hits']:
    if 'Failed' in doc['_source']['message']:
        print("{} --- {}".format(doc['_id'], doc['_source']['message']))

