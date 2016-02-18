from random import randint


class shootOut():
	def __init__play(self, player):
		self.player = player
		health = 100
	
	if health >= 0:
		print"Press s to shoot"
		Answer = raw_input(">  ")
		if Answer == 's':
			print "You shot the Gothon"
			damage = randint(10,33)
			health = health - damage 
		else:
			print "Sorry press S to shoot"
	elif health >= 1:		
			print "Gothons health is %d:" % health
	else:
		print "you killed the Gothon! Good work"	


#---------------------------------

class Duel:
	def __init__(self, player):
		self.player = player
		
class shootOut(Duel):
	def __init__(self, name, health):
		self.name = name
		self.health = health
	health = 100
	
	
	while health >= 0:
		print"Press s to shoot"
		Answer = raw_input(">  ")
		if Answer == 's':
			print "You shot the Gothon"
			damage = randint(10,33)
			health = health - damage
			print "Gothons health is %d:" % health
		else:
			print "Sorry press S to shoot"			
	print "you killed the Gothon! Good work"




you = Duel
gothon = Duel
Duel.you
Duel.gothon






#time to make this in to a class system

#call one class for person and one for the Gothon then run them alternatively intil one wins and print a suitable statement! you died or you killed the Gothon!
play()
