import requests as re
import pprint as p

url1 = "https://api.github.com/users/cod-lab/repos?sort=created"
pyload = {'sort': 'created'}


response = re.get('https://api.github.com/users/cod-lab/repos',params=pyload)

print(type(response))
result = response.json()
print(type(result))
print(len(result))

for i in range(len(result)):
    # print(i)  
    pprint(result[i])
    
    
# print(result['full_name'])
# p.pprint(r.json())

