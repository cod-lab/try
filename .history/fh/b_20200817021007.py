import requests as r
import pprint as p

url1 = "https://api.github.com/users/cod-lab/repos?sort=created"
pyload = {'sort': 'created'}


r = r.get('https://api.github.com/users/cod-lab/repos',params=pyload)

print(type(r))

print(r.)