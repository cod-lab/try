import requests as re
import pprint as p

url1 = "https://api.github.com/users/cod-lab/repos?sort=created"
pyload = {'sort': 'created'}


r = re.get('https://api.github.com/users/cod-lab/repos',params=pyload)

print(type(r))

p.pprint(r.json())