import json
import facebook

with open('secrets.json') as f:
    secrets = json.load(f)



#graph = facebook.GraphAPI(app_secret=secrets['app_secret'], version="23.0")
graph = facebook.GraphAPI(secrets['access_token'], version="23.0")

profile = graph.get_object('me',fields='first_name,last_name,location,link,email')  
print(json.dumps(profile, indent=5))

events = graph.request('type=event&limit=10000')
print(events)