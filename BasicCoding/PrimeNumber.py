from math import sqrt
def factorsCount(n):
    c=0
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            c+=1 
    return c
num=int(input())
if factorsCount(num)==0:
    print("Prime number")
else:
    print("Not a prime number")