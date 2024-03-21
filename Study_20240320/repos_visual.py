
import requests
import plotly.express as px

url = 'https://api.github.com/search/repositories?q=language:python+sort:stars'

response = requests.get(url)
data = response.json()

items =data.get('items',[])

names=[]
stars=[]

for item in items:
    name = item.get('name')
    star = item.get('stargazers_count')

names.append(name)
stars.append(star)


# res=requests.get(url)
# print((res.json()))

# dicts = res['items']
# names=[]
# stars=[]
# for dict in dicts:
#     names.append(dicts['name'])
#     stars.append(dicts['stars'])
    
fig = px.bar(x=names, y=stars)
fig.show()

# with open('./Study_20240320/repositories.json', 'r',encoding='utf-8') as f :
#     res = json.loads(f)
#     print(res)
    # print(len(res['items']. type[res['items']]))
    # for item in res['items']:
    #     names.append(item['name'])
    #     stars.append(item['starazers_count'])


# items=[]
# x=[]
# star=[]

# for res_item in res[x]:
# x.append(res.json['total_count'][1])
# print(x)`