str="I am Jasna"
l=len(str)
def countupper():
    c = 0
    for i in range(0,l):
        if str[i].isupper()==True:
            c+=1
    print("count of uppercase letter {}".format(c))
countupper()
def countlower():
    c = 0
    for i in range(0,l):
        if str[i].islower()==True:
            c+=1
    print("count of lowercase letter {}".format(c))
countlower()