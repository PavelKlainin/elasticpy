



#res = es.search(index=today, body={"query": {"match_all": {}}})
#res = es.search()
#print(res)

#print('{} documents found'.format(res['hits']['total']))
#print(res['hits']['hits'])

regex_ip = re.compile(r'([0-9]{1,3}\.){3}[0-9]{1,3}')

ip_who_attack = {}

for doc in res['hits']['hits']:
    if 'sshd' in doc['_source']['message']:
        ip = regex_ip.search(doc['_source']['message']).group()
        if ip in ip_who_attack:
            ip_who_attack.update({ip: ip_who_attack[ip]+1})
        else:
            ip_who_attack.update({ip: 1})
print(ip_who_attack)
        #print(ip, doc['_source']['@timestamp'])
        #print("At Host {} --- {}".format(doc['_source']['beat']['hostname'], doc['_source']['message']))
        #if regex_ip in

