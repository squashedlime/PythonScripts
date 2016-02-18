class Parent(object):
	def altered(self):
		print "PARENT altered()"

class Child(Parent):
	def altered(self):
		print "child, before parent altered()"
		super(Child, self).altered()
		print "Child, After parent altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
