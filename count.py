list=["hi","how","hah","python","neven"]
c=0
for x in list:
    if len(x)>=2 and x[0]==x[-1]:
        c+=1
print(c)