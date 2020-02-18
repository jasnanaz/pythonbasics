num=input('enter a number')
rev=0
while num>0:
    reverse=(reverse*10)+reminder
    num=num//10
    print(reverse)
if num==reverse:
    print("palindrome")
else:
    print("not palindrome")