import math

class Line():

	def __init__(self,coor1=(0,0),coor2=(0,0)):
		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):
		return math.sqrt((self.coor2[0]-self.coor1[0])**2+(self.coor2[1]-self.coor1[1])**2)

	def slope(self):
		if self.coor2[0]-self.coor1[0] == 0:
			return 0
		else:
			return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])

new_line = Line()
print(new_line.distance())
print(new_line.slope())

new_line = Line((3,2),(8,10))
print(new_line.distance())
print(new_line.slope())