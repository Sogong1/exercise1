def fib(n):
	sum = 1
	while(n>0):
		sum = sum*n
		n -= 1
		return sum

result = fib(10)
printf(result)
