num=int(input())
x=num
s=0
while(x):
    s=s*10+x%10 
    x//=10 
print(f"Reverse of {num} is:",s)