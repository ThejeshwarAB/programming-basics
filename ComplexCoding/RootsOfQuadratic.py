from math import sqrt
a=int(input())
b=int(input())
c=int(input())
d=(b**2)-(4*a*c)
f=0
if(d>0):
    # real roots 
    r1=(-b+sqrt(d))/(2*a)
    r2=(-b-sqrt(d))/(2*a)
elif d==0:
    # equal roots 
    r1=-b/(2*a) 
    r2=r1 
else:
    # imaginary roots
    r11=-b/(2*a) 
    r21=r11 
    r12=(sqrt(-d))/(2*a)
    r22=r12 
    f=1
if f==0:
    print(r1,r2) 
else:
    print(f"{r11}+{r12} {r21}-{r22}")