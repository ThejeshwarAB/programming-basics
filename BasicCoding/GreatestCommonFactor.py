a,b=map(int,input().split())
mini=a if a<b else b 
for i in range(1,mini+1):
    if a%i==0 and b%i==0:
        gcd=i 
print("GCD is:",gcd)