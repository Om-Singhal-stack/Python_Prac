n = input("enter a number")

c = len(n)
int(n)

for i in range(0,c):
    rem = n%10
    sum = sum + (rem**c)
    n = n/10

if(sum==l):
    print("armstrong number")
else:
    print("not armstrong number")