import requests as re
import pprint as p

url1 = "https://api.github.com/users/cod-lab/repos?sort=created"
pyload = {'sort': 'created'}


response = re.get('https://api.github.com/users/cod-lab/repos',params=pyload)

# print(type(r))

for i in 5:
    
    
result = response.json()

# print(result['full_name'])
# p.pprint(r.json())

