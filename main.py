import json
import http
import facebook

with open('secrets.json') as f:
    secrets = json.load(f)

conn = http.client.HTTPSConnection('graph.facebook.com')
conn.request(method = 'GET', 
            url = '/oauth/access_token?client_id=' + secrets['app_id'] + '&client_secret=' + secrets['app_secret'] + '&grant_type=client_credentials',
            headers= {'User-Agent':'curl/7.68.0'} 
            )
response = conn.getresponse()
print(response.status, response.reason)
data = response.read()
conn.close()

jsondata = json.loads(data)
access_token = jsondata['access_token']

graph = facebook.GraphAPI(access_token, version="3.1")

profile = graph.get_object('me',fields='first_name,last_name,location,link,email')  
print(json.dumps(profile, indent=5))

'''
events = graph.request('type=event&limit=10000')
print(events)
'''