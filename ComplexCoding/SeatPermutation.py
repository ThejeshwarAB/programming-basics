def factorial(x):
	if x==1:
		return x 
	else:
	 	return x*factorial(x-1)
n=int(input())
r=int(input())
p=factorial(n)/factorial(n-r)
print(f"{n} people can occupy {r} seats in {p} ways")