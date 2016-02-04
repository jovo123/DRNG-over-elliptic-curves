import random
from affineEdwards import *
from affineWeierstrass import *

class powerGenerator:

	def affine(curve):	
		e = random.randint(2, curve.group_order)
		for n in range (1, 21):
			W_n = curve.mult(curve.Gx, curve.Gy, e**n)
			return W_n[0]

	def projective(curve):	
		e = random.randint(2, curve.group_order)
		for n in range (1, 21):
			W_n = curve.mult(curve.Gx, curve.Gy, curve.Gz, e**n)
			rn = curve.toAffine(W_n)[0]
			return rn
