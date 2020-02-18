list=[1,2,1,1,1]
list.append(4)  #append 4 to list
print(list)
a=list.count(1)   # count a particilar number
print(a)
print(list[1]) #ccess list elemrnts second
print(list[-1]) #access last element
print(list[-2]) #aceess second last element only
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")#insert at first index
print(thislist)
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")   #remove banana
print(thislist)
thislist = ["apple", "banana", "cherry"] #remove cheery
thislist.pop()
print(thislist)
thislist = ["apple", "banana", "cherry"]  #remove 0 index
del thislist[0]
print(thislist)
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)  #make a new copy of above list
