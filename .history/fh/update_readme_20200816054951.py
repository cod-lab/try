# f=open('a.md','r')
# print(f.name)
# print(f.)
# f.close()

# Method 1 : Context Manager
with open('README.md','r') as f:
    for lines in f:
        print(lines, end='')
        
