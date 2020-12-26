octal=int(input())
decimal=0
i=0
dummy=octal
while(dummy):
    r=dummy%10
    decimal+=r*int(pow(8,i))
    i+=1
    dummy//=10
print(f"Decimal equivalent of {octal} is: {decimal}")