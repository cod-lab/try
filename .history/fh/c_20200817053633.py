import fileinput as fi
import requests as r
import pprint as p
import sys as s


def read_file(file):
    with open(file,'r') as f:
        for i, line in enumerate(f):
            if 37<i<43:
                current_list[i] = line


def get_repos_list():
    payload = {'sort': 'created'}
    response = r.get('https://api.github.com/users/cod-lab/repos',params=pyload)
    result = response.json()        # got list of all repos
    
    # getting filtered list (latest 5 repos which r not forked)
    new_list={}
    j=-1
    for i in range(len(result)):
        if result[i]['fork'] == False:
            new_list[i+37] = "* [" + result[i]['name'] + "](" + result[i]['html_url'] + ")"
            j+=1
        
        if j==4: break


def write_file(file):
    for line in fi.FileInput(file,inplace=1):
        for i in current_list:
            if current_list[i] == line:
                line = new_list[i+37]+"\n"
                # line=str(new[i-38])+"\n"
        print(line,end='')


file = 'a.md'
current_list={}
new_list={}
read_file(file)

if current_list[38] != new_list[38]: write_file(file)