import json
from datetime import datetime
from datetime import timedelta


data = open('data.json').read()

messages = json.loads(data)
list_date = []

for item in messages:
    list_date.append(item)

user_1 = []
user_2 = []
for user_for in list_date:
    if user_for['user'] == 'U1ZQR43RB':
        user_1.append(user_for)
    else:
        user_2.append(user_for)

list_user1 = []
list_user2 = []
append_list_user1 = []
append_list_user2 = []
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
        append_list_user1.insert(0, str(time_after))

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
        append_list_user2.insert(0, str(time_after))



arquivo = open('U0MFNAG05.json', 'w')
arquivo.close()

arquivo = open('U0MFNAG05.json', 'w')
list_user1[0].insert(0, "2016-08-13 14:54:46.000005")
for x in list_user1:
    arquivo.write(str(x)+"\n")
arquivo.close()

arquivo = open('U0KK0T3CG.json', 'w')
arquivo.close()

arquivo = open('U0KK0T3CG.json', 'w')
list_user2[0].insert(0, "2016-08-13 14:54:45.000002")
for x in list_user2:
    arquivo.write(str(x)+"\n")
arquivo.close()
