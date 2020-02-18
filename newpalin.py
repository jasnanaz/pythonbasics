snum=input('enter a number')
num=int(snum)
temp=num
reverse=0
while num>0:
    reminder=num%10
    reverse=(reverse*10)+reminder
    num=num//10
if temp==reverse:
    print("palindrome")
else:
    print("not palindrome")

