binary=int(input())
decimal=0 
i=0 
dummy=binary
while(dummy):
    r=dummy%10
    decimal+=r*int(pow(2,i))
    i+=1
    dummy//=10 
print(f"Decimal equivalent of {binary} is: {decimal}")