n=int(input("enter a number"))
a=n
rev= 0
while n > 0:
    digit= n%10
    rev= rev*10+digit
    n=n//10
if a == rev:
    print("its a palindrome")
else:
    print("it isnt")    