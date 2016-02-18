import random
import time
import random

def weaponChoice(n):
	print "make weapons choice: "
	print " 1 - blaster" + "\n" + "2 - shooter" + "\n" + "3 - rocket launcher" + "\n"
	weapon = raw_input(">")

	if weapon == "1":
		return  (5,30)
	elif weapon == 2:
	 	return (25,50)
	elif weapon == 3:
		return (75,90)
	else:
		print "sorry choose 1,2,3"

def end(you_health, goth_health):
		if goth_health < 1:
				print "...you killed the Gothon!!"
				print "good job" 
				exit()
				 
		elif you_health < 1:
				print quip() + "\n" +"The Gothon did you in!!"	
				exit()
weapon = weaponChoice(n)

def quip():
	quips = ["he blew your leg off!", 
				"well there went your head!",
				"you melt into a pool of jelly!"]
	print (random.choice(quips))
	
				 
	#how to get the values from weapon into line44?? come on .....

def play():
	you_health = 100
	goth_health = 100
 	while goth_health >= 0 and you_health >=0:
		weaponChoice()
		print"Press s to shoot"
		Answer = raw_input(">  ")
		if Answer == 's':
			print "You shot the Gothon"
			damage = random.randrange(weaponChoice)
			print damage
			goth_health = goth_health - damage
			if goth_health < 1:
				end(you_health, goth_health)
			print "Gothons health is %d:" % goth_health	
			time.sleep(2)
			print "The Gothon shoots back!"
			damage = randint(20,35)
			you_health = you_health - damage
			if you_health < 1 :
				print quip()
				end(you_health, goth_health)
			print "you were hit, your health is %d" % you_health
		else:
			print "Sorry press S to shoot"
	#return goth_health, you_health



		
			
play()

