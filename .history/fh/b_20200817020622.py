import requests


pyload = {'sort': 'created'}
url = "https://api.github.com/users/cod-lab/repos?sort=created"


r = requests.get('https://api.github.com/users/cod-lab/repos',params=pyload)
