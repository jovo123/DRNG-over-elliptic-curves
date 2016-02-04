def egcd(a, b):
	if a == 0:
		return(b, 0, 1)
	else:
        	g, y, x = egcd(b % a, a)
        	return (g, x - (b // a) * y, y)

def fieldInv(g, p):
	#want yg = 1 (mod p) => yg = 1 + xp
	gcd, x, y = egcd(g,p)
	if gcd != 1:
		return None
	else:
		return x % p

#print fieldInv(22,29)
