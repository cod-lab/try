import requests as re
import pprint as p

url1 = "https://api.github.com/users/cod-lab/repos?sort=created"
pyload = {'sort': 'created'}


response = re.get('https://api.github.com/users/cod-lab/repos',params=pyload)

print(type(response))
result = response.json()
print(type(result))
print(len(result))

repos1={}
repos2=[[]]

for i in range(len(result)):
    # print(i)  
    # print(i,result[i]['name'])
    # repos[i] = [result[i]['name']]
    # repos[i]['name'] = result[i]['name']
    
    repos1[i] = {'name': result[i]['name'], 'html_url': result[i]['html_url']}
    repos2[i] += [
        ['name',result[i]['name']],
        ['html_url',result[i]['html_url']]
    ]
    # repos[i] += {'html_url': result[i]['html_url']}
    
# print(result['full_name'])
# p.pprint(r.json())

p.pprint(repos)

