def fibo(n):
	if (n == 1 or n == 2): return 1;
	else: return fibo(n-1) + fibo(n-2);

n = input("insert a number: \n")
print "Fibonacci of ", n ," is: "

ans = 1
cur = 1
prev = 1
for i in range(2,n):
	ans = cur + prev
	prev = cur
	cur = ans
print ans
