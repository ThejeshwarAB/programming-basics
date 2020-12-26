def factorial(n):
    s=1 
    for i in range(1,n+1):
        s*=i 
    return s
num=int(input())
x=num
y=0 
while(x):
    y+=factorial(x%10)
    x//=10  
if y==num:
    print("Strong number")
else:
    print("Not a strong number")