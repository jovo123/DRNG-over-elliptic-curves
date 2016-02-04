#jacobian projective coordinates
#char(K) != 2, 3
#E: y^2 = x^3 + ax + b
import math 
from GFp import *
class projWeierstrass:
	
	a = -3
	b = 0
	group_order = 0
	field_order = 0
	Gx = 0
	Gy = 0
	Gz = 0

	def __init__(self, field_order, curve_order, param_a, param_b, gx, gy, gz):
                self.field_order = field_order
                self.group_order = curve_order
                self.a = -3
                self.b = param_b
                self.Gx = gx
                self.Gy = gy
		self.Gz = gz	

	def neg(X, Y, Z):
		return (X, -1*Y, Z)

	def double(self, X, Y, Z):
		if X == 1 and Y == 1 and Z == 0:
			return (X,Y,Z)
		
		T1 = Z*Z  
		T2 = X - T1 
		T1 = X + T1
		T2 = T2 * T1
		T2 = 3*T2
		Y3 = 2*Y
		Z3 = Y3*Z
		Y3 = Y3**2
		T3 = Y3 * X
		Y3 = Y3**2
		Y3 - Y3/2
		X3 - T2**2
		T1 = 2*T3
		X3 = (X3 -T1) % self.field_order

		T1 = T3 -X3		
		T1 = T1*T2
		Y3 = (T1 - Y3) % self.field_order
		return(X3, Y3, Z3)

	def add(self, X1, Y1, Z1, x2, y2):
		if X1 == 1 and Y1 == 1 and Z1 == 0: return(x2, y2, 1)
		if (x2 == "infinity"): return(X1, Y1, Z1)
		T1 = Z**2
		T2 = T1*Z1
		T1 = T1*x2
		T2 = T2*y2
		T1 = T1-X1
		T2 = T2-Y1
		if(T1 == 0):
			if(T2 == 0):
				(X3,Y3,Z3) = self.double(x2,y2,1)
				return (X3,Y3,Z3)
			else: return (1,1,0)
		Z3 = Z1*T1
		T3 = T1**2
		T4 = T3*T1
		T3 = T3*X1
		T1 = 2*T3
		X3 = T2**2
		X3 = X3 - T1
		X3 = (X3 - T4) % self.field_order

		T3 = T3 - X3
		T3 = T3*T2
		T4 = T4*Y1
		Y3 = (T3 - T4) % self.field_order
		return(X3,Y3,Z3)

	def multiply(self, X, Y, Z, n):
		X3 = X
		Y3 = Y
		Z3 = Z
		if X == X3 and Y == Y3 and Z == Z3:
			(X3, Y3, Z3) = self.double(X,Y,Z)
		for _ in range(0,n):
			(X3, Y3, Z3) = self.add(X,Y,Z,X3,Y3,Z3)
		return(X3, Y3, Z3)

	def toAffine(self,X,Y,Z):
		zInv = fieldInv(Z,self.field_order)
		x = (X * zInv**2) % self.field_order
		y = (Y * zInv**3) % self.field_order
		return(x,y)



