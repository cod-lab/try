# f=open('a.md','r')
# print(f.name)
# print(f.)
# f.close()

# Method 1 : Context Manager
with open('a.md','r') as f:
    for i,line in enumerate(f[38:43]):
        if i==38:
            print(i, line)

    # if f.tell() == 
    # for lines in f:
    #     print(lines, end='')
    
    for lines in f:
        if f.tell() == 4:
            print(lines)
            
