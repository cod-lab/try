import fileinput as fi
import requests as r
import pprint as p
import sys as s


# Get Current List
def read_file(file,current_list):
    with open(file,'r') as f:
        for i, line in enumerate(f):
            if 37<i<43:
                current_list[i] = line


# Get New List
def get_repos_list(new_list):
    payload = {'sort': 'created'}
    response = r.get('https://api.github.com/' + users +' /cod-lab/repos',params=payload)
    result = response.json()        # got list of all repos

    if len(result)<5: s.exit("Error: less than 5 repos available")
    
    # getting filtered list (latest 5 repos which r not forked)
    j=1
    for i in range(len(result)):
        if result[i]['fork'] == False:
            new_list[j+37] = "* [" + result[i]['name'] + "](" + result[i]['html_url'] + ")"
            j+=1
        if j>5: break


# OverWrite New List to file if there's any difference
def write_file(file,current_list,new_list):
    for line in fi.FileInput(file,inplace=1):
        for i in current_list:
            if current_list[i] == line:
                line = new_list[i]+"\n"
        print(line,end='')



user='cod-lab'
file = 'a.md'
current_list={}
new_list={}

read_file(file,current_list)
get_repos_list(new_list)

print("current_list: ")
p.pprint(current_list)
print("\nnew_list: ")
p.pprint(new_list)

diff=0
for i in range(5):
    if current_list[i+38] != new_list[i+38]: diff+=1

print("\ndiff: ",diff,"\n")
if diff>0: write_file(file,current_list,new_list)
