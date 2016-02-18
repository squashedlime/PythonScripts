#!/bin/python

from sys import exit
from random import randint

class Scene(object):
	"the scene class is the base class"
	def enter(self):
		exit(1)

class Engine(object):
#simple start with the __init__ self.variable is equal to variable
	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
#fixing a way to know where you are
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while True:
			print "\n------------"
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)
		current_scene.enter()
		
class Death(Scene):
	#this is a list
	quips = [
		"You died. You kind suck at this!!.",
		"your mom would be proud ...if she was smarter!!",
		"What a looooser!"
		"I have a small puppy that's better than you!"
	]

	def enter(self):
	#this will randomly print a death text you could also write
	#import random
	#print(random.choice(quips))
		print Death.quips[randint(0, len(self.quips)-1)]
		exit(1)


class CentralCorridor(Scene):

	def enter(self):
		print "The Gothons of Planet Percal #25 have invaded your ship and destroyed"
		print "your entire crew. You are the last surviving member and your last"
		print "mission  is to get the neutron destruct bomb from the Weapons Armory."
		print "put it in the brigde, and blow the ship up after getting into an "
		print "escape pod."
		print "\n"
		print "You're running down the central corridor to the Weapons Armory when"
		print "a Gothon jumps out, red scaly skin, dark grimy teeth and evil clown costume"
		print "flowing around his hate filled body. He's blocking the door to the"
		print "Amoury and about to pull a weapon to blast you."

		action = raw_input("> ")

		if action == "shoot!":
			print "Quick on the draw, you yank out your blaster.."
			return 'death'

		elif action == "dodge!":
			print "like a streak of lightning you dodge the Gothons laser"
			return 'death'

		elif action == "Tell a joke":
			print "luckily you did your Gothons training and know the deadly uibnct joke"
			print "It roles off your touge in Gothon --blaoih veoifj b09w4 osf sif i "
			print "The Gothon starts to split in to pieces with laughter"
			print "and melts...you jump over the mess into the Amoury"
			return 'laser_weapon_armory'

		else:
			print "DOES NOT MAKE SENSE...ARE YOU TYPING IN GOTHON?"
			return 'central_corridor'



class LaserWeaponArmory(Scene):

	def enter(self):
		print "you dive into a roll and land in the Weapons Armory, crouch and"
		print "scan the room for more gothons. It's quiet..too quiet!"
		print "you see the nuetron bomb on the other side of the room."
		print "There's a keypad lock on it's container. You need to guess the"
		print "code to disarm the bomb. you get 10 attempts, the code is 3 digits"
		code = "%d%d%d%" % (randint(1,9), randint(1,9), randint(1,9))
		guess = raw_input("[keypad]> ")
		guesses = 0

		while guess != code and guesses < 10:
			print "bzzzzzzedddd"
			guesses += 1
			guess = raw_input("[keypad]> ")

		if guess == code:
			print "the keypad flashes and the seal to the bomb opens"
			print "you grabb the nuetron bomb and run as fast as you can to"
			print "to the bridge, You must place it in the right spot."
			return 'the bridge'
		else:
			print "the lock buzzes one last time and the last thing you see"
			print "is the bomb starting to fuse together, Blowing your ship up"
			return 'death'


class TheBridge(Scene):

	def enter(self):
		print "You bust on to the brigde with the neutron bomb"
		print "under you arm and surprise 5 Gothans who are trying to"
		print "take control of the ship. They hesitate to draw their weapons"
		print "because they see the armed bomb and don't want to set it off."

		action = raw_input("> ")

		if action == "throw the bomb":
			print "In a panic you throw the bomb at the group of Gothons"
			print "and make a leap for the door. Just as you reach the door"
			print "a laser hits you in the back and you die, the ship is blown"
			print "up by the bomb."
			return 'death'

		elif action == "slowly":
			print "you point your laser at the bomb under your arm"
			print "The Gothons put their hands up and start to sweat!"
			print "you inch backwards and place the bomb on the floor still"
			print "pointing your laser at it you open the door and slip out"
			print "now the bomb is placed you have to make it to the escape pod"
			return 'escape_pod'
		else:
			print "DOSE NOT COMPUTE!"
			return 'the_bridge'

class EscapePod(Scene):

	def enter(self):
		print "you run through the ship desparately trying to make it to"
		print "the escape pod before the whole ship explodes. you reach"
		print "the escape pod area. Some of them could be damaged. Which"
		print "one do you take?"

		god_pod = randint(1, 5)
		guess = raw_input("[pod #]> ")

		if int(guess) != good_pod:
			print "you jump into po number %d and press eject" % guess
			print "it fires you out into space where the pod implodes"
			print "due to a damaged hull"
			return 'death'

		else:
			print "you jump into pod number %d and press eject" % guess
			print "it flies in to void of space and takes you to the"
			print "planet. you look back to see the ship explode"
			print "blowing up the Gothons ship as well you WON!!"

			return 'finished'

class Finished(Scene):

    def enter(self):
        print "you won!good job."
        return 'finished'


class Map(object):
#this is a dict
	scenes = {
		'central_corridor': CentralCorridor(),
		'laser_weapon_armory' : LaserWeaponArmory(),
		'the_bridge' : TheBridge(),
		'escape_pod' : EscapePod(),
		'death' : Death(),
		'finished' : Finished(),
	}

	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
	    val = Map.scenes.get(scene_name)
	    return val


	def opening_scene(self):
		return self.next_scene(self, start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
