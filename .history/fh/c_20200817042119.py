import fileinput as fi
import requests as r
import pprint as p
import sys as s

def read_file():
    with open('a.md','r') as f:
        for i, line in enumerate(f):
            if 37<i<43:
                temp[i] = line