the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#this first kind of for loop goes through a list
for numbers in the_count:
	print "This is count %d" % numbers
	
#same as above
for f in fruits:
	print "A fruit of type: %s" % f
	
#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" % i

# we can also build lists, first start with an empty one
print "now we are going to create a list"
elements = []
#then use the range function to do 0 to 5 counts

for i in range(0, 4):
	print "Adding %d to the list." % i
	#append, is a function, that lists understand
	elements.append(i)

print "\nnow we'll print it"
#now we can print them out too
for i in elements:
	print "Elements was: %d" % i
print "And has %d number of elements: " % len(elements)
