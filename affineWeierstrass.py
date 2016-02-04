#affine coordinates
#char(K) != 2, 3
#E: y^2 = x^3 + ax + b
import math 
from GFp import *
import itertools
class affineWeierstrass:	
	#order of prime - 1 base field
	field_order = 0
	#prime order of curve
	group_order = 0
	#parameters
	a = 0
	b = 0
	#base point x, and y coorinates
	Gx = 0 
	Gy = 0

	def __init__(self, field_order, curve_order, param_a, param_b, gen_x, gen_y):
		self.field_order = field_order
		self.group_order = curve_order
		self.a = param_a
		self.b = param_b
		self.Gx = gen_x
		self.Gy = gen_y

	def add(self, x1, y1, x2, y2):
		#check identity
		if x1 == "infinity": 
			return(x2, y2)
		if x2 == "infinity":
			return(x1, y1)
		#check inverse
		if(x1 == x2 and y1 == -y2):
			return (0, 0)
		#check equality
		if(x1 == x2 and y1 == y2):
			return self.double(x1, y1)
		else:
		#	print "adding!"
			m = (y2 - y1) * fieldInv(x2 - x1, self.field_order)
			x3 = ((m**2) - x1 - x2)%self.field_order
			y3 = (m*(x1 - x3) - y1)%self.field_order
			return (x3, y3)


	def double(self, x, y):
		#print "doubling!"
		m = (3*(x**2) + self.a) * fieldInv(2*y, self.field_order)
		x3 = (m**2 - 2*x)%self.field_order
		y3 = (m*(x - x3) - y)%self.field_order
		return (x3, y3)

	def mult(self, x, y, n):
		x3 = x
		y3 = y
		for i in itertools.count(n):
			if x3 == x and y3 == y:
				(x3, y3) = self.double(x, y)
			else:
				self.add(x3, y3, x, y)
		return (x3, y3)
#E = affineWeierstrass(29, 37, 4, 20, 2, 6)
#print E.add(5,22,16,27)
#print E.double(5,22)
