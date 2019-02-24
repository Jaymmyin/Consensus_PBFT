# python2.x
import json
import urllib2

data = {
    "clientID":"ahnhwi",
    "operation":"GetMyName",
    "timestamp":859381532
}

req = urllib2.Request('http://localhost:11101/req')
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))
res = response.read()
print(res)