decimal=int(input())
binary=0
i=0
dummy=decimal
while(dummy):
    r=dummy%2
    binary+=r*int(pow(10,i))
    i+=1
    dummy//=2
print(f"Binary equivalent of {decimal} is: {binary}")