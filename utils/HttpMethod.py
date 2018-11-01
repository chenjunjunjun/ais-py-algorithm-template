import requests
import json
from urllib import request

def http_get(url,params=None):
    if params is None:
        r=requests.get(url)
    else:
        r=requests.get(url,params=params)
    data=json.loads(r.text)
    return data,r.status_code

def http_post(url,data,headers=None): 
    data=json.dumps(data).encode('utf-8')
    if headers is None:          
        req = request.Request(url, data)      
    else:
        req = request.Request(url, data,headers=headers)
    response = request.urlopen(req) 
    response=response.read().decode('utf-8')      
    r=json.loads(response)
    return r

def http_put(url,data):
    if data is None:
        r=requests.put(url)
    else:
        r=requests.put(url,data=data)
    data=json.loads(r.text)
    return data,r.status_code

def http_delete(url,iid):
    r=requests.delete(url+'/'+iid)
    return r.status_code