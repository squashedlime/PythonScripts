def testof_return(a, b):
	print "the total of %d + %d is:" % (a, b)
	return a + b
prompt = '>>'	
print "ok enter your values"
first = float(raw_input(prompt))
print "ok enter another"
second = float(raw_input(prompt))

print testof_return(first, second)

