
#n = 8


def while_loop(n, s):
	i = 0
	numbers = []

	while i < n:
		print "At the top is %d" % i
		numbers.append(i)
	
		i = i + s
		print "Numbers now:", numbers
		print "At the bottom i is %d" % i


		print "The numbers:"
		
	for num in numbers:	
			print num

#while_loop(25, 5)

