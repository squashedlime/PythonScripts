#!/usr/bin/python 

S = [x**2 for x in range(10)] #global variable with name S

#remember variables in function blocks are only locally accessible by the function they are not global.
def choice_a(x):
	print(S)
	return

def choice_b(x):
	V = [2**i for i in range(x)]
	print (V)
	return # this just exits the function 

def choice_c(y):
	M = [x for x in range(y) if x % 2 == 0]
	print (M)
	
def choice_d():
	exit(0)
	
print ('Which operation do you want to perform?\n')
print ('''
a: X to the second power
b: 2 the xth power
c: mod 2
d: quit program
''')

resp = input('choices: ')
resp2 = int(input('Upper limit? '))

# conditional logic ..it's compact becuase it is embedding function blocks!! This part has to be after the functions and variables because Python reads from the top down!
if resp == 'a':
	choice_a(resp2) #using choice_a and parsing in the resp2 as an argument
elif resp == 'b':
	choice_b(resp2)
elif resp == 'c':
	choice_c(resp2)
else:
	choice_d()
	
	
