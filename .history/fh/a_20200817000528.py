import fileinput as fi

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
for line in fi.input("a.md",inplace=1):
    if 38<fi.lineno()<44:
        # line=line+
        temp[fi.lineno()] = line
        print(temp[fi.lineno()],end='')

pprint(temp)