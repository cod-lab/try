import requests as re
import pprint as p
import sys as s

url1 = "https://api.github.com/users/cod-lab/repos?sort=created"
pyload = {'sort': 'created'}


response = re.get('https://api.github.com/users/cod-lab/repos',params=pyload)

p.pprint(response.json()[0]['full_name'])
print(len(response.json()))

print(type(response))
result = response.json()
print(type(result))
print(len(result))

print("respone size: ",s.getsizeof(response.json()))
print("result size: ",s.getsizeof(result))

print(response.json()[1]['fork'])

# repos1={}
repos2=[[],[[],[]]]
# repos3=[[],[[],[]]]
temp={}

j=-1
for i in range(len(response.json())):
    # print(i)  
    # print(i,result[i]['name'])
    # repos[i] = [result[i]['name']]
    # repos[i]['name'] = result[i]['name']
    if response.json()[i]['fork'] == False:
        # repos1[i] = {'name': result[i]['name'], 'html_url': result[i]['html_url']}
        repos2 += [[[i],{'name': response.json()[i]['name'],'html_url': response.json()[i]['html_url']}]]
        
        temp[i+37] = "* [" + result[i]['name'] + "](" + result[i]['html_url'] + ")\n"
        
        # repos3 += [[[i],['name',result[i]['name']],['html_url',result[i]['html_url']]]]
        j+=1
    if j==4: break

# print(result['full_name'])
# p.pprint(r.json())

# p.pprint(repos1)
print("\n")
p.pprint(temp)
print("\n")
p.pprint(repos2[2:])

print(temp[38] )
# for i in repos2

# repos2 += [[[i],{'name': result[i]['name'],['html_url',result[i]['html_url']]}]]
