import fileinput as fi
import requests as r
import pprint as p
import sys as s



# Get Current List
def read_file(file,current_list):
    with open(file,'r') as f:
        for i, line in enumerate(f):
            # if 37<i<43:
            current_list += [[line]]              # current_list[i] = current_list[i][:-1]             # also works-1


# Get New List
def get_repos_list(user,new_list):
    payload = {'sort': 'created'}
    # response = re.get('https://api.github.com/users/cod-lab/repos?sort=created, timeout=10)           # also works
    response = r.get('https://api.github.com/users/' + user + '/repos', params=payload, timeout=10)
    result = response.json()        # got list of all public repos

    # getting filtered list (latest 5 public repos which r not forked)
    j=1
    for i in range(len(result)):
        if result[i]['fork'] == False:
            # new_list[j+37] = "* [" + result[i]['name'] + "](" + result[i]['html_url'] + ")\n"
            current_list[j+38] = ["* [" + result[i]['name'] + "](" + result[i]['html_url'] + ")\n"]
            j+=1
        if j>5: break

    # if len(new_list)<5: s.exit("\nError: less than 5 repos available")          # terminate prgm right away after printing msg


# OverWrite New List to file if there's any difference
def write_file(file,current_list,new_list):
    with open(file,'w') as f:
        for x in current_list:
            f.write(str(x))


user='cod-lab'
file='a.md'
current_list=[[]]
new_list={}

print('\nread_file block----------------------\n')
try: read_file(file,current_list)
except FileNotFoundError: s.exit('No such file!!\nEnter correct file name..')          # terminate prgm right away after printing msg
print('\nread_file block end------------------\n')

print('\nget_repos block----------------------\n')
try: get_repos_list(user,new_list)
except r.exceptions.ConnectTimeout: s.exit('The server is not responding currently!!\nPlease try again later..')    # problem connecting srvr or srvr not responding   # terminate prgm right away after printing msg
except r.exceptions.ReadTimeout: s.exit('The server is not responding currently!!\nPlease try again later..')   # unable to read received response  # terminate prgm right away after printing msg
print('\nget_repos block end------------------\n')

# '''
print("current_list: ")
# p.pprint(current_list, indent=2)#, width=3)
for i in range(len(current_list)):
    print(i,current_list[i])
'''print("\nnew_list: ")
p.pprint(new_list, indent=2, width=3)
'''

'''
diff=0
for i in range(5):
    if current_list[i+38] != new_list[i+38]: diff+=1

print("\ndiff: ",diff,"\n")
if diff>0:
'''
print('\nwrite_file block----------------------\n')
write_file(file,current_list,new_list)
print('\nwrite_file block end------------------\n')
# '''