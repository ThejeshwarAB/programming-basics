a,b=map(int,input().split())
maxi=a if a>b else b 
for i in range(maxi,a*b+1):
    if i%a==0 and i%b==0:
        lcm=i 
        break
print("LCM is:",lcm)