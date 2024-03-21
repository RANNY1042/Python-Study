import json
import plotly.express as px

# json # load - csv reader와 같이 file
# json # loads - str -> dict, dict-> str

mag =[]
lat =[]
lon =[]


with open('C:\python\Study_20240320\geodata\eq_data_7_day_m1.geojson','r', encoding='utf-8') as f:
    data = json.load(f)
    print(type(data), type(data['features']), data['features'][0])
    
    for feature in data['features']:
        # print(feature['properties']['mag'],type(feature['properties']['mag']))
        mag.append(feature['properties']['mag'])
        lon.append(feature['geometry']['coordinates'][0])
        lat.append(feature['geometry']['coordinates'][1])      
                   
    
    #  print(type(data), type(data['features'],data['features'][0]))
    # print(type(data), type(data['metadata']),type(data['metadata']['count']))
    # print(data['features'][0]['properties']['mag'])
    
    # print(data['features'][0]['geometry']['coordinates'])

fig=px.scatter_geo(lat=lat, lon=lon, size=mag)
fig.show()


# for i in [1,2,3,4]:
#     print(i)