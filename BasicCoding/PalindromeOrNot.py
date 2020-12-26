num=int(input())
x=num 
y=0
while(x):
    y=y*10+x%10 
    x//=10 
if y==num:
    print("Palindrome")
else:
    print("Not a palindrome")