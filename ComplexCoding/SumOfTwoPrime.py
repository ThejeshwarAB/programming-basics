from math import sqrt
def isPrime(x):
	f=1
	for i in range(2,int(sqrt(x))+1):
		if x%i==0:
			f=0
			break
	return f 

num=int(input())
f=0
for i in range(2,num):
	if isPrime(i) and isPrime(num-i):
		f=1 
		break
if f==1:
	print("Can be expressed in sum of two primes")
else:
	print("Cannot be expressed in sum of two primes")