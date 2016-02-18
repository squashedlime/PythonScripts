class MyClass2:
	age = 0
	title = "noname"
	Names = []
	#this method adds a new name to the Names list
	def add(self, name):
		self.Names.append(name)
	
def Main():
	#set me to MyClass2()
	me = MyClass2()
	me.title = "jason" #now we have set the name attribute to jason
	me.age = 12  #now we have set the number attribute to 12345
	
	friend = MyClass2() #and repeat with friend
	friend.title = "steve"
	friend.age = 3
	
	fr_list = MyClass2()#create an object of MyClass2
	#calling th add function/method and adding new names to the list
	fr_list.add("jason")
	fr_list.add("peter")
	fr_list.add("Amber")
	
	
	
	
	print "Name: " + me.title + ", Present Age: " + str(me.age)
	print "Name: " + friend.title + ", Present Age:  " + str(friend.age)
	print "Name list: " + str(fr_list.Names)
	
if __name__ == '__main__':
	Main()
