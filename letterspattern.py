from __future__ import print_function
num=65
for i in range(1,5):
    for j in range(0,i,1):
        a=chr(num)
        print(a,end=" ")
        num+=1

    print(' ')