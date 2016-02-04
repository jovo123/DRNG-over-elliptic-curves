import random
from random import randint
from affineEdwards import *
from affineWeierstrass import *

# input: 
# (a, b) or d curve parameters
# p = order of base field
# N = order of elliptic curve group is prime
# l | N - 1 
# G = (xg, yg) of order l

# generate a random n-dimensional vector a = (a1, ... an), ai in Z/lZ
# find a random integer x = x1x2...xn in range [0,2^n-1]


# output random x coord of pt on curve
def NRaffine(curve):
	alpha = []
	n = 5
	for i in range (0, n):
		alpha.append(randint(0, curve.group_order))
	x = randint(0,2**n - 1)
	binx = x | 0b000000
	binx = bin(x)[2:]
	k = 1
	for i in range(0, n):
		k *= alpha[i] ** int(binx[i])
		random = curve.mult(curve.Gx, curve.Gy, k)
		print random[0]

def NRprojective(curve):
	alpha = []
	n = 5
	for i in range (0, 5):
		alpha.append(randint(0,curve.group_order))
	x = randint(0,2**n - 1)
	binx = x | 0b000000
	binx = bin(x)[2:]
	k = 1
	for i in range(0, 5):
		k *= alpha[i]** int(binx[i])
		random = curve.mult(curve,Gx, curve.Gy, k)
		random = curve.toAffine(random)
		return random
