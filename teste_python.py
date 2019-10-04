import json
from datetime import datetime
from datetime import timedelta

date = open('data.json').read()
dates = json.loads(date)

managers = []
watchers = []

for dados in dates:
    for x in dados['managers']:
        if x not in managers:
            managers.append(x)
            locals()['manager_%s' %x]=[]
    for y in dados['watchers']:
        if y not in watchers:
            locals()['watchers_%s' %y]=[]
            watchers.append(y)

for dados in dates:
    for x in dados['managers']:
        for y in managers:
            if x == y:
                locals()['manager_%s' %x].append((dados['name'],dados['priority']))
                locals()['manager_%s' %x].sort(key=lambda x: x[1])
                    
    for x in dados['watchers']:
        for y in watchers:
            if x == y:
                locals()['watchers_%s' %x].append((dados['name'],dados['priority']))
                locals()['watchers_%s' %x].sort(key=lambda x: x[1])

for user in managers:
    locals()['managerof_%s' %user] = []
    for x in locals()['manager_%s' %user]: 
        locals()['managerof_%s' %user].append(x[0])
for user in watchers:
    locals()['watchersof_%s' %user] = []
    for x in locals()['watchers_%s' %user]: 
        locals()['watchersof_%s' %user].append(x[0])

manager = {}
watcher = {}

for x in managers:
    manager[x] = locals()['managerof_%s' %x]
for y in watchers:
    watcher[y] = locals()['watchersof_%s' %y]

with open('managers.json', 'w') as json_file:
    json.dump(manager, json_file, indent=2)  

with open('watchers.json', 'w') as json_file:
    json.dump(watcher, json_file, indent=2)        
