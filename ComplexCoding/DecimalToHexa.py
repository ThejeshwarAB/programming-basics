hexa="0123456789ABCDEF"
decimal=int(input())
dummy=decimal
val=""
while(dummy):
    r=dummy%16 
    val+=hexa[r]
    dummy//=16 
val=val[::-1]
print(f"Hexa equivalent of {decimal} is: {val}")