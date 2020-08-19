import fileinput as fi
import pprint as p
import urllib
# for line in fi.FileInput("a.md",inplace=1):
#     print(line)
    
    
# for i,line in enumerate(fi.FileInput("a.md",inplace=1)):
# # for line in fi.FileInput("a.md",inplace=1):
#     # print(line, end='')
#     if 37<i<43:
#         # print(i+1, line, end='')
#         # print("type of line: ",type(line))
#         # line=""
#         print("deleted")



new=[1,2,3,4,5]
temp={}
# for line in fi.input("a.md"):
#     if 38<fi.lineno()<44:
#         temp[fi.lineno()] = line
#         # print(temp[fi.lineno()],end='')

# READING
with open('a.md','r') as f:
    for i, line in enumerate(f):
        if 37<i<43:
            temp[i+1]=line

# WRITING
for line in fi.FileInput("a.md",inplace=1):
    for i in temp:
        if temp[i] == line:
            line=str(new[i-37])+"\n"
    print(line,end='')

# p(temp)
p.pprint(temp)
