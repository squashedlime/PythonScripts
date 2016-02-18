#define the class Song
class Song(object):
# method 	
	def __init__(self, lyrics):
		self.lyrics = lyrics
# 	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
#defining the class here we set the variable happy_bday to Song its only variable
happy_bday = Song(["Happy birthday to you",
					"I don't want to get sued",
					"So I'll stop right now"])
#so here we set the variable happy_bday to Song its only variable
bulls_on_parade = Song(["They rally around the family",
						"With pockets full of shells"])
#call the happy_bday variabel with the sing_me_a_song method from the Song class	
happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
