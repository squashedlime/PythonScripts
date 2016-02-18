import random

def weaponChoice():
	print "Make weapons choice: "
	print "\n1 - blaster" + "\n" + "2 - shooter" + "\n" + "3 - rocket launcher" + "\n"
	
	weapon = raw_input(">")
	weappwr = {1: "5,30", 2: "25,50", 3: "75,90"}
	for value, pwr in weappwr.items():
		if value == weapon:
			return pwr

print pwr[pwr]
#print weappwr["weapon"]

''' if weapon == "1":
		return 5, 20")
	elif weapon == "2":
	 	return (25, 50)
	elif weapon == "3":
		return (75, 90)
	else:  '''
# print "sorry choose 1,2,3"
weaponChoice()
