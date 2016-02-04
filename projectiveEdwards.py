#projective coordinates
#E: x^2 + y^2 = 1 + d x^2 y^2

from GFp import *
class projEdwards:

	d = 0
	field_order = 0
	group_order = 0
	Gx = 0
	Gy = 0
	Gz = 0

	def __init__(self, param, g_ord, f_ord, gx, gy, gz):	
		self.d = param
		self.group_order = g_ord
		self.field_order = f_ord
		self.Gx = gx
		self.Gy = gy
		self.Gz = gz

	def add(x1, y1, z1, x2, y2, z2):
		#check identity
		if x1 == 0 and y1 == 1 and z1 == 1:
			return(x2, y2, z2)
		if x2 == 0 and y2 == 1 and z2 == 1:
			return(x1, y1, z1)
		#check inverse
		if x1 == (-1*x2) and y1 == y2 and z1 == z2:
			return (0, 1, 1)
		else:
			A = x1 * z2
			B = y1 *z2
			C = z1 * x2
			D = z1 * y2
			E = A*B
			F = C*D
			G = E + F
			H = E - F
			J = (A - C)*(B + D) - H
			K = (A + D)*(B + C) - G
			x3 = (G*J)%self.field_order
			y3 = (H*K)%self.field_order
			z3 = (J*K*d)%self.field_order
			return (x3, y3, z3)
	
	def mult(self, X, Y, Z, n):
		X3 = X
		Y3 = Y
		Z3 = Z
		for _ in range(0,n):
			(X3,Y3,Z3) = self.add(X3,Y3,Z3,X,Y,Z)
		return (X3,Y3,Z3)

	def toAffine(self, X, Y, Z):
		zInv = fieldInv(Z, self.field_order)
		x = (X*zInv) % self.field_order
		y = (Y*zInv) % self.field_order
		return (x,y)
