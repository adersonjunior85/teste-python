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

manager = {}
watcher = {}
print(locals()['manager_%s' %x])
for x in managers:
    manager[x] = locals()['manager_%s' %x]


with open('manager.json', 'w') as json_file:
    json.dump(manager, json_file, indent=1)        







'''
messages = json.loads(data)
list_date = []
list_time = []

for message in messages:
    if message["user"] not in list_date:
        list_date.append(message["user"])
        list_time.append(message["ts"])
        locals()['usuario_%s' %message['user']]=[]
        locals()['listuser_%s' %message['user']]= []

for message in messages:
    for user in list_date:
        if message['user'] == user:
            locals()
            locals()['listuser_%s' %message['user']].append(message)

for user in list_time:
    time_now = float(time)/60
    for message in locals()['listuser_%s' %user]:
        time_message = (float(message['ts']))/60
        if time_message >= time_now and time_message <= (time_now+2):
            print(user)
            print(time_message)
            print(time_now)
                
                
        else:
            time_now+=2 
        

#print(listuser_U0KK0T3CG)
    

'''
        



'''
for user_for in list_date:
    if user_for['user'] == 'U0MFNAG05':
        user_1.append(user_for)
    elif user_for['user'] == 'U0KK0T3CG':
        user_2.append(user_for)
    elif user_for['user'] == 'U1ZQR43RB':
        user_3.append(user_for)
    else:
        user_4.append(user_for)



list_user1 = []
list_user2 = []
list_user3 = []
list_user4 = []
append_list_user1 = []
append_list_user2 = []
append_list_user3 = []
append_list_user4 = []

cont1 = 894.75
for user_for1 in user_1:
    time_after = datetime.fromtimestamp(float(user_for1['ts']))
    time = (time_after.hour*60)+time_after.minute+(time_after.second/60)
    if time >= cont1 and time <= (cont1+2):
        append_list_user1.append(user_for1)

    else:
        list_user1.append(append_list_user1)
        append_list_user1 = []
        new_count = datetime.fromtimestamp(float(user_for1['ts']))
        cont1 = (new_count.hour*60)+new_count.minute+(new_count.second/60)
        append_list_user1.append(user_for1)
        append_list_user1.insert(0, str(user_for1['ts']))

cont1 = 894.75
for user_for2 in user_2:
    time_after = datetime.fromtimestamp(float(user_for2['ts']))
    time = (time_after.hour*60)+time_after.minute+(time_after.second/60)
    
    if time >= cont1 and time <= (cont1+2):
        append_list_user2.append(user_for2)

    else:
        list_user2.append(append_list_user2)
        append_list_user2 = []
        new_count = datetime.fromtimestamp(float(user_for2['ts']))
        cont1 = (new_count.hour*60)+new_count.minute+(new_count.second/60)
        append_list_user2.append(user_for2)
        append_list_user2.insert(0, str(user_for2['ts']))
list_user2.append(append_list_user2)
append_list_user2 = []
new_count = datetime.fromtimestamp(float(user_for2['ts']))
cont1 = (new_count.hour*60)+new_count.minute+(new_count.second/60)
append_list_user2.append(user_for2)
append_list_user2.insert(0, str(user_for2['ts']))

cont1 = 894.76
for user_for3 in user_3:
    time_after = datetime.fromtimestamp(float(user_for3['ts']))
    time = (time_after.hour*60)+time_after.minute+(time_after.second/60)
    
    if time >= cont1 and time <= (cont1+2):
        append_list_user3.append(user_for3)

    else:
        list_user3.append(append_list_user3)
        append_list_user3 = []
        new_count = datetime.fromtimestamp(float(user_for3['ts']))
        cont1 = (new_count.hour*60)+new_count.minute+(new_count.second/60)
        append_list_user3.append(user_for3)
        append_list_user3.insert(0, str(user_for3['ts']))

cont1 = 896.9833333333333
for user_for4 in user_4:
    time_after = datetime.fromtimestamp(float(user_for4['ts']))
    time = (time_after.hour*60)+time_after.minute+(time_after.second/60)
    
    if time >= cont1 and time <= (cont1+2):
        append_list_user4.append(user_for4)

list_user4.append(append_list_user4)
append_list_user4 = []
new_count = datetime.fromtimestamp(float(user_for4['ts']))
cont1 = (new_count.hour*60)+new_count.minute+(new_count.second/60)
append_list_user4.append(user_for4)
append_list_user4.insert(0, str(user_for4['ts']))




arquivo = open('U0MFNAG05.json', 'w')
arquivo.close()

arquivo = open('U0MFNAG05.json', 'w')
list_user1[0].insert(0, "1471110885.000002")
for x in list_user1:
    arquivo.write(str(x)+"\n")
arquivo.close()

arquivo = open('U0KK0T3CG.json', 'w')
arquivo.close()

arquivo = open('U0KK0T3CG.json', 'w')
list_user2[0].insert(0, "1471110885.000003")
for x in list_user2:
    arquivo.write(str(x)+"\n")
arquivo.close()

arquivo = open('U1ZQR43RB.json', 'w')
arquivo.close()

arquivo = open('U1ZQR43RB.json', 'w')
list_user3[0].insert(0, "1471110886.000005")
for x in list_user3:
    arquivo.write(str(x)+"\n")
arquivo.close()

arquivo = open('USLACKBOT.json', 'w')
arquivo.close()

arquivo = open('USLACKBOT.json', 'w')
list_user4[0].insert(0, "1471111019.937810")
for x in list_user4:
    arquivo.write(str(x)+"\n")
arquivo.close()
'''