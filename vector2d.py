class Vector2d:
	
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
	def __add__(self, other) #this is a special method
		return Vector2d(self.x + other.x, self.y + other.y)
	
	def __iadd__(self, other):
		self.x += other.x
		self.y += other.y
		return self
	
	def __sub__(self, other):
		return Vector2d(self.x - other.x, self.y - other.y)
	
	def __isub__(self, other):
		self.x -= other.x
		self.y -= other.y
		return self
		
def Main():
	vec = Vector2d(5, 6)
	print "x:" + str(vec.x) + ",Y:" + str(vec.y)

if __name__ == '__main__':
	Main()
