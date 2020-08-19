import fileinput as fi
import pprint as p

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

temp={}
for line in fi.FileInput("a.md"):
    if 38<fi.lineno()<44:
        temp[fi.lineno()] = line
        # print(temp[fi.lineno()],end='')

for line in fi.FileInput("a.md",inplace=1):
    for i in temp:
        if temp[i] in line:
            line="deleted"
        print(line)

# p(temp)
# p.pprint(temp)