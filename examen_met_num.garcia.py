import math

def funcion(x):
	return math.cos(x) - math.pow(x,3);

def derivadafuncion(x):
	return -math.sin(x) - (3.0 * x * x);

i = int (0);

x = float (input('Cual es el valor de x:'));
tmp = 0;

while (x != tmp and i < 100):

	temp = x;
	x = x - funcion(x) / derivadafuncion(x);
	a = abs ((x- tmp) / x);

	print('x' + str(i) + ' " ' + str(x) + 'Error = ' + str(a) + '\n');
	i = i + 1;

if (i == 100):
	print('\n\n No Se Encuentra ');
else:
	print('\n\n Resultado x:' + str(x));




