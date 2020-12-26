octal=int(input())
decimal=0
i=0
dummy=octal
while(dummy):
    r=dummy%10
    decimal+=r*int(pow(8,i))
    i+=1
    dummy//=10
binary=0
i=0
dummy=decimal
while(dummy):
    r=dummy%2
    binary+=r*int(pow(10,i))
    i+=1
    dummy//=2
print(f"Binary equivalent of {octal} is: {binary}")