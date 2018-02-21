def fibo(n):
	if (n == 1 or n == 2): return 1;
	else: return fibo(n-1) + fibo(n-2);

n = input("insert a number: \n")
print "Fibonacci of ", n ," is: "
print fibo(n)
