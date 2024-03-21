import csv
import datetime 
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime as dt


x1=[]
y1=[] 

x2=[]
y2=[] 

with open('Study_20240315\weather_data\sitka_weather_07-2021_simple.csv') as f:
# with open(Path('data','Study_20240315\weather_data\sitka_weather_07-2021_simple.csv')) as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
        # print(line, type(line))
        COL_DATAE = 2
        x1.append(line[COL_DATAE])
        COL_TMAX = 4
        y1.append(line[COL_TMAX])
        
        new_var2 = 2
        x2.append(line[new_var2])
        new_var3 = 5
        y2.append(line[new_var3])
    
    print(f'x:{x1}')
    print(f'x: {y1}')

    for idx , h  in enumerate(header):
        print(idx, h)
    
    plt.plot(x1,y1, label='TMAX')
    plt.plot(x2,y2, label='TMIN')
    plt.fill_between(x1,y1,y2, alpha=0.1)
    plt.xticks(rotation=80)
    plt.legend()
    plt.show()

