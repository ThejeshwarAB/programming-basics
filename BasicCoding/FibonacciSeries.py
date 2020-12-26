n=int(input())
f,s=-1,1 
for i in range(n):
    print(f+s,end=' ')
    t=f+s 
    f=s 
    s=t 