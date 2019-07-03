import math
import numpy 

fx = lambda x: x**2 - sin x**3 

a = 1
b = 2
tolerancia = 0.5


p =[]
distacia = b-a 

fa = fx(a)
fb = fx (b)
i = 1

while (distacia>tolerancia):
	c = (a+b)/2
	fc = fx(c)
	p.appendi([i,a,c,b,fa,fc,distacia])
	i = i+1

	change = np.sign(fa)*np.sign(fc)
	if (change < 0):
		b = c
		fb = fc
	else:
		a = c
		fa = fc
	distacia = b-a
	
c =(a+b)/2
fc = fx(c)
p.appendi([i,a,c,b,fa,fc,fb,distacia])

raiz = c 

np.set_printoptions (precision = 4)
print('[i,a,c,b,f(a),f(c),f(b),pass')

n= len (p)
for in range (0,n,1):
	f1 = p[i]
	tipe = '{:.0f}'+''+(len(f1)-1)*'{:.3f}'
	f1 = tipe.format(*f1)
	print (f1)


print ('raiz: ',raiz)		