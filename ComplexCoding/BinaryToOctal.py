binary=int(input())
decimal=0 
i=0 
dummy=binary
while(dummy):
    r=dummy%10
    decimal+=r*int(pow(2,i))
    i+=1
    dummy//=10 
octal=0
i=0
dummy=decimal
while(dummy):
    r=dummy%8
    octal+=r*int(pow(10,i))
    i+=1
    dummy//=8
print(f"Octal equivalent of {binary} is: {octal}")