n = int(input("enter how many terms you want"))
a=0
b=1

print(a,b,end=" ")
for i in range(3,n):
    next = a+b
    print(next,end=" ")
    a=b
    b=next