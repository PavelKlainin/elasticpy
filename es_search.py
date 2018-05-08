from datetime import datetime
import re
from connector import es_connect

es = es_connect()

def es_search():
    today = datetime.strftime(datetime.now(), 'filebeat-%Y.%m.%d')
    # res = es.search(index=today, body={'query': {'prefix': {'message': 'sshd'}}})
    res = es.search(index=today, body={'query': {'match': {'message': 'Failed password'}}})