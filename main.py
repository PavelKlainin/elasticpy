from elasticsearch import Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

import requests
res = requests.get('http://localhost:9200')
print(res.content)