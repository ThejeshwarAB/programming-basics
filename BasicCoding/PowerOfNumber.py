def power(n,x):
    if x==1:
        return 1 
    else:
        return n*power(n,x-1)
num,exp=map(int,input().split())
print(f"{num}^{exp}={power(num,exp)}")