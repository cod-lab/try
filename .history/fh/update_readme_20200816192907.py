# f=open('a.md','r')
# print(f.name)
# print(f.)
# f.close()

# Method 1 : Context Manager
with open('a.md','r') as f:
    # print("len f:", len(f))
    for i,line in enumerate(f):
        if 37<i<43:
        # for i in range(38,43):
            print(i+1, line, end='')

    # if f.tell() == 
    # for lines in f:
    #     print(lines, end='')
    
    for lines in f:
        if f.tell() == 4:
            print(lines)
            
