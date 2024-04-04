import pandas as pd
landmark = pd.DataFrame({'name':['광화문','호미곶','첨성대'],
                         'location':['서울 종로구 사직로 161',
                                     '경북 포항시 남구 호미곶면 대보리 150',
                                     '경북 경주시 인왕동 839-1']})

print(landmark['location'].str[3:6])

print(landmark['location'].str.split(" ",expand=True))

landmark['loc_1'] = landmark['location'].str.split(" ").str[0]
print(landmark['loc_1'])

print(landmark['location'].str.startswith('서울'))
print(landmark['location'].str.endswith('1'))
print(landmark['location'].str.contains('1'))

from datetime import datetime

print(datetime.today())
print(datetime.today().year)

print(datetime.strptime('2022-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))

time = datetime.today()
print(time.strftime('%Y-%m-%d %H:%M:%S'))

from datetime import timedelta
time = datetime.today()
print(time + timedelta(days=100))


