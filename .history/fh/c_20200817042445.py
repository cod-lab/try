import fileinput as fi
import requests as r
import pprint as p
import sys as s

def read_file():
    with open('a.md','r') as f:
        for i, line in enumerate(f):
            if 37<i<43:
                temp[i] = line

def write_file():
    for line in fi.FileInput('a.md',inplace=1):
        for i in temp:
            if temp[i] == line:
                line=str(new[i-38])+"\n"
        print(line,end='')

def get_repos_list():
    