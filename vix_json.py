import json

with open('vix-daily_json.json', 'r') as vix:
    data=vix.read()

obj = json.loads(data)

print(obj['High'])




