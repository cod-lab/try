import requests


url1 = "https://api.github.com/users/cod-lab/repos?sort=created"
pyload = {'sort': 'created'}


r = requests.get('https://api.github.com/users/cod-lab/repos',params=pyload)

print(r)

print(r.)