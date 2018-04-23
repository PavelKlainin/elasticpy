from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': '192.168.7.5', 'port': 9200}])

#print(es.info())

#print(es.get(index="filebeat-2018.04.23", doc_type="doc", id='uC-y8mIBAt7Av6H3m_mc'))
a = es.search(index='filebeat-2018.04.23', body={"query": {"prefix" : { "message" : "pass" }}})


# for k, v in a:
#     if k == 'system message':
#         print(v)

#import requests
#res = requests.get('http://192.168.7.5:9200')
#print(res.content)