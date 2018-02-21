def maxsubseq(ar):
	n = len(ar)
	current_max = 0
	global_max = -1000000
	for i in range(0,n):
		current_max += ar[i]
		if(current_max > global_max):
			global_max = current_max
		if(current_max < 0):
			current_max = 0
		
	return global_max;

ar = [2, 3, -1, 10, 11, -2]
print maxsubseq(ar)
