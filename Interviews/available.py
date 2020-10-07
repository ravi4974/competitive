import datetime,functools

calendar_data={
    'user1':[
        {
            'name':'meeting1',
            'from':datetime.datetime(2019,12,14,9,30),
            'to':datetime.datetime(2019,12,14,11,30)
        },
        {
            'name':'meeting2',
            'from':datetime.datetime(2019,12,14,14,30),
            'to':datetime.datetime(2019,12,14,16,30)
        }
    ],
    'user2':[
        {
            'name':'meeting1',
            'from':datetime.datetime(2019,12,14,9,30),
            'to':datetime.datetime(2019,12,14,12,00)
        },
        {
            'name':'meeting2',
            'from':datetime.datetime(2019,12,14,13,00),
            'to':datetime.datetime(2019,12,14,15,30)
        }
    ],
    'user3':[
        {
            'name':'meeting1',
            'from':datetime.datetime(2019,12,14,9,00),
            'to':datetime.datetime(2019,12,14,10,30)
        },
        {
            'name':'meeting2',
            'from':datetime.datetime(2019,12,14,14,30),
            'to':datetime.datetime(2019,12,14,15,30)
        }
    ]
}

timeslot={
    'from':datetime.datetime(2019,12,14,9,00),
    'to':datetime.datetime(2019,12,14,18,00)
}

def get_available_hours(meetings):
    slots=[]
    #start of timeslot
    if len(meetings)>0 and meetings[0]['from']>timeslot['from']:
        slots.append({'from':timeslot['from'],'to':meetings[0]['from']})
    #in between meetings
    for i in range(0,len(meetings)-1):
        if meetings[i+1]['from']>meetings[i]['to']:
            slots.append({'from':meetings[i]['to'],'to':meetings[i+1]['from']})
    #end of the timeslot
    if meetings[len(meetings)-1]['to']<timeslot['to']:
        slots.append({'from':meetings[len(meetings)-1]['to'],'to':timeslot['to']})
    return slots

available_hours=[get_available_hours(calendar_data[user]) for user in calendar_data]

def compare(t1,t2):
    slots=[]
    for x in t1:
        for y in t2:
            f=max([x['from'],y['from']])
            t=min([x['to'],y['to']])
            if f>t: continue
            slots.append({'from':f,'to':t})
    return slots

print(functools.reduce(lambda a,b: compare(a,b),available_hours))