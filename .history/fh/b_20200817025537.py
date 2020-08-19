import requests as re
import pprint as p

url1 = "https://api.github.com/users/cod-lab/repos?sort=created"
pyload = {'sort': 'created'}


response = re.get('https://api.github.com/users/cod-lab/repos',params=pyload)

print(type(response))
result = response.json()
print(type(result))
print(len(result))

repos=[]
for i in range(len(result)):
    # print(i)  
    # print(i,result[i]['name'])
    repos[i] = [['name']result[i]['name']]
    # repos[i]['name'] = result[i]['name']
# print(result['full_name'])
# p.pprint(r.json())

print(repos)

