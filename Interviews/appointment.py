import datetime

meeting_data=[
    {
        'name':'meeting1',
        'from':datetime.datetime(2019,12,14,10,30,00),
        'to':datetime.datetime(2019,12,14,11,30,00)
    },
    {
        'name':'meeting2',
        'from':datetime.datetime(2019,12,14,17,30,00),
        'to':datetime.datetime(2019,12,14,18,00,00)
    },
    {
        'name':'meeting3',
        'from':datetime.datetime(2019,12,14,12,00,00),
        'to':datetime.datetime(2019,12,14,12,30,00)
    },
    {
        'name':'meeting4',
        'from':datetime.datetime(2019,12,14,14,30,00),
        'to':datetime.datetime(2019,12,14,16,30,00)
    },
    {
        'name':'meeting5',
        'from':datetime.datetime(2019,12,14,10,30,00),
        'to':datetime.datetime(2019,12,14,11,00,00)
    },
    {
        'name':'meeting6',
        'from':datetime.datetime(2019,12,14,9,30,00),
        'to':datetime.datetime(2019,12,14,11,00,00)
    }
]

sorted_meeting_data=sorted(meeting_data,key=lambda x: x['from'])

#print(sorted_meeting_data)

for i in range(1,len(sorted_meeting_data)):
    if sorted_meeting_data[i]['from']<sorted_meeting_data[i-1]['to']:
        print(sorted_meeting_data[i]['name'],'has conflict with ',sorted_meeting_data[i-1]['name'])