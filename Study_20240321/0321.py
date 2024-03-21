import pandas as pd
landmark = pd.DataFrame({'name':['광화문','호미곶','첨성대'],
                         'location':['서울 종로구 사직로 161',
                                     '경북 포항시 남구 호미곶면 대보리 150',
                                     '경북 경주시 인왕동 839-1']})

landmark['location'].str[3:6]