decimal=int(input())
octal=0
i=0
dummy=decimal
while(dummy):
    r=dummy%8
    octal+=r*int(pow(10,i))
    i+=1
    dummy//=8
print(f"Octal equivalent of {decimal} is: {octal}")