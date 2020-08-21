import requests as r
import pprint as p
import sys as s
import ast as a
import json


# Get Current List
def read_file(file,content):
    with open(file,'r') as f:
        temp={}
        temp=json.load(f)
        print(/"temp: \n",temp)
        for line in f:
            content += [[line]]              # content += [line[:-1]]             # also works-1


# Get New List
def get_repos_list(user,content):
    old_content=content+[]

    # print("\ncontent0: ")
    # for i in range(1,len(content0)):
    #     print(i,content0[i][0][:-1])
    
    # response = re.get('https://api.github.com/users/cod-lab/repos?sort=created, timeout=10)           # also works
    payload = {'sort': 'created'}
    result = r.get('https://api.github.com/users/' + user + '/repos', params=payload, timeout=0.0010).json()
    # result = response.json()        # got list of all public repos

    # getting filtered list (latest 5 public repos which r not forked)
    j=1
    for i in range(len(result)):
        if result[i]['fork'] == False:
            content[j+38] = ["* [" + result[i]['name'] + "](" + result[i]['html_url'] + ")\n"]
            j+=1
        if j>5: break

    if j<5: s.exit("\nError: less than 5 repos available")          # terminate prgm right away after printing msg

    # print("\ncontent: ")
    # for i in range(1,len(content)):
    #     print(i,content[i][0][:-1])


    # for i in range(5):
    #     diff=0
    #     if content[i+39] != old_content[i+39]: diff+=1
    #     print("\ndiff: ",diff,"\n")
    #     if diff>0: 
    #         print('\nwrite_file block----------------------\n')
    #         write_file(file,content)
    #         print('\nwrite_file block end------------------\n')            
    #         break

    if content != old_content:
        print('\nwrite_file block----------------------\n')
        write_file(file,content)
        print('\nwrite_file block end------------------\n')


# OverWrite New List to file if there's any difference
def write_file(file,content):
    with open(file,'w') as f:
        for i in range(1,len(content)):
            f.write(content[i][0])              # f.write(content[i][0][:-1])             # also works-1



user='cod-lab'
file='a.md'
content=[[]]


print('\nread_file block----------------------\n')
try: read_file(file,content)
except FileNotFoundError: 
    # # errs = open("logs",'r')#.read()#logs.open().read
    z="logs"

    err = {}
    err['datenow()']="1no such file"

    errs = a.literal_eval(open(z,'r').read())
    errs.update(err)

    # errs.update(err)
    print(errs)

    open(z,'w').write(str(errs))
    # f.write(temp)

    # open("w").write(err)
    
    # z='logs'
    # errs={}
    # f = open(z,"r")
    # errs = a.literal_eval(f.read())
    # f.close()
    
    # err = {}
    # err['datenow()2']="no such file"
    
    # print(errs)
    # errs.update(err)
    # print(errs)
    # f = open(z,"w")
    # f.write(str(errs))
    # f.close()
    
    s.exit('No such file!!\nEnter correct file name..or create one!')          # terminate prgm right away after printing msg
print('\nread_file block end------------------\n')


print('\nget_repos block----------------------\n')
try: get_repos_list(user,content)
except r.exceptions.ConnectTimeout: s.exit('The server is not responding currently!!\nPlease try again later..')    # problem connecting srvr or srvr not responding   # terminate prgm right away after printing msg
except r.exceptions.ReadTimeout: s.exit('Unable to read response received from requested api currently!!\nPlease try again later..')   # unable to read received response  # terminate prgm right away after printing msg
except r.exceptions.ConnectionError: s.exit('Your internet is not working currently!!\nPlease try again later..')   # unable to read received response  # terminate prgm right away after printing msg
print('\nget_repos block end------------------\n')


# print("content: ")
# p.pprint(content, indent=2)#, width=3)
# for i in range(1,len(content)):
#     print(i,content[i][0][:-1])


# print('\nwrite_file block----------------------\n')
# write_file(file,content)
# print('\nwrite_file block end------------------\n')
