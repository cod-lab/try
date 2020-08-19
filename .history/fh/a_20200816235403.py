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

temp=[]
for line in fi.input("a.md",inplace=1):
    if 37<fi.lineno()<43:
        temp[fi.lineno]+=line
        
print(temp)