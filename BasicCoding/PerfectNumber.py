num=int(input())
s=0 
for i in range(1,num+1):
    if num%i==0:
        s+=i 
if s==2*num:
    print("Perfect number")
else:
    print("Not a perfect number")