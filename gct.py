a= int(input("enter a num"))
b= int(input("enter a num"))
while b:
    x= b
    b= a % b
    a= x
print(a)    