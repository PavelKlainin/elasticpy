from elasticsearch import Elasticsearch as ES
import sys


def es_connect():
    try:
        es = ES([{'host': '192.168.7.5', 'port': 9200}])
        #print('Connected', es.info())
        return es
    except Exception as ex:
        print('Error: ', ex)
        sys.exit()