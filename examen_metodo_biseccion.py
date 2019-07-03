from math import sin,cos,tan,asin,acos,atan,sqrt,log,exp
from math import sinh,cosh,tanh,asinh,acosh,atanh
print('Bisseccion\n')
ec=input('De la funcion a resolver: ')  
x0=float(input('Extremo inferior aproximado: '))
x1=float(input('Extremo superior aproximado: '))
tamaño_del_error=float(input('Tamaño del error: '))
 

def f(x):
    return eval(ec)

 
while True:
    xmed=(x0+x1)/2
    fxmed=f(xmed)
    if fxmed==0.0:
        break
 
    if (f(x1)*f(xmed))<0:
        x0=x0
        x1=xmed
    else:
        x0=xmed
        x1=x1
    error=abs(x1-x0)
    if error<tamaño_del_error:
        break
 

print ('La raíz es',xmed)
input(' ')
