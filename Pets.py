class Pet:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def talk(self):
		raise NotImplementedError('Subclass must implement abstract method')

class Cat(Pet): #this inherits from pet
	def __init__(self, name, age):
		Pet.__init__(self, name, age) #this a calling the initialisatoin of the superclass
		
	def talk(self):
		return "meow"

class Dog(pet):
	
	def __init__ (self, name, age)
		Pet.__init__(self, name, age)
		
	def talk(self)
		return "woof"
		
def Main():
	
	"""thePet = Pet("Pet", 1) #create an object
	jess = Cat("jess" , 3) #create object nr 2 both inherit from Pet class
	
	print "is jess a cat?" + str(isinstance(jess, Cat)) #using the is instance function is instance of jess a cat
	print "is jess a Pet?" + str(isinstance(jess, Pet))
	print "is thePet a Cat?" + str(isinstance(thePet, Cat))
	print "is thePet a Pet?" + str(isinstance(thePet, Pet))
	
	print jess.name"""
	
	pets = [Cat("jess", 2).dog("jack", 7), Cat("fred", 2), Pet("thePEt", 5)]
	
	for 
	
if __name__ == "__main__":
	Main()
