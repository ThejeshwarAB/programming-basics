num=int(input())
x=num 
y=num 
c=0 
s=0 
while(x):
    x//=10 
    c+=1 
while(y):
    s+=(y%10)**c 
    y//=10 
if s==num:
    print("Armstrong number") 
else:
    print("Not an armstrong number")