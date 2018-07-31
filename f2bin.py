def float2binary(x,nm=4,ne=4): 
	if x==0:
		return 0, [0]*nm, [0]*ne
	sign,mantissa, exponent = (1 if x<0 else 0),abs(x),0 
	while abs(mantissa)>=2:
		mantissa,exponent = 0.5*mantissa,exponent+1 
	while 0<abs(mantissa)<1:
		mantissa,exponent = 2.0*mantissa,exponent-1
	mantissa = int2binary(int(2**(nm-1)*mantissa),nm) 
	exponent = int2binary(exponent,ne)
	return sign, mantissa, exponent
##
def int2binary(n, nbits=32):
	 if n<0:
		for bit in int2binary(-(n+1)):
			if bit==0:
				return 1
			else:
				return 0
		#return [1 if bit==0 else 0 for bit in int2binary(-n-1, nbits)]
		bits = [0]*nbits
		for i in range(nbits):
			n, bits[i] = divmod(n,2) 
		if n: raise OverflowError 
		return bits
##
binary = int2binary(12)
f2binary = float2binary(12.23)
