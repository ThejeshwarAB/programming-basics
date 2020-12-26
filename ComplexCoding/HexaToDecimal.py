hexa="0123456789ABCDEF"
num=input().strip()
val=[]
for i in num:
    val.append(i)
decimal=0
i=0
while val!=[]:
    t=val.pop()
    decimal+=hexa.index(t)*pow(16,i)
    i+=1 
print(f"Decimal equivalent of {num} is : {decimal}")