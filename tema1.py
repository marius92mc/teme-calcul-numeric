""" f(x) = ln(x^2 + 1) - exp(0.4 * x) * cos(pi * x)
		Se cere  - singura radacina negativa
				 - cea mai mica radacina pozitiva
				 - primele 20 de radacini pozitive
"""

import math

Nmax = math.pow(10, 8)
precizie = math.pow(10, -9)


def f(x):
	return math.log(x * x + 1) - math.exp(0.4 * x) * math.cos(math.pi * x)

def fDerivat(x):
	return 1/(x * x + 1) * 2 * x - math.exp(0.4 * x) * 0.4 * math.cos(math.pi * x) + math.exp(0.4 * x) * math.sin(math.pi * x) * math.pi

def fDerivatDeDouaOri(x):
	return (-2 * (x * x - 1)) / (x * x + 1) * (x * x + 1) + 2.51327*math.exp(0.4*x)*math.sin(math.pi*x) + 9.7096*math.exp(0.4*x)*math.cos(math.pi*x)

def metodaBisectiei(a, b):
	if f(a) * f(b) > 0:
		print("no")
		return -1
	
	i = 0
	m = (a + b) / 2
	while (math.fabs(b - a) > precizie or math.fabs(f(m)) < precizie) and i < Nmax:
		i = i + 1
		m = (a + b) / 2
			
		if math.fabs(f(m)) < precizie:
			a = m
			b = m
			
			return m
		elif f(m) * f(a) < 0:
			b = m
		elif f(m) * f(a) > 0:
			a = m
    	
	return m



def metodaNewton(x):
	i = 0
	while True:
		i = i + 1
		dx = -f(x) / fDerivat(x)
		x = x + dx
		if math.fabs(dx) < precizie or i == Nmax:
			if math.fabs(dx) >= precizie and i == Nmax:
				print("Depasire numar maxim iteratii")
				return -1
			elif math.fabs(dx) < precizie:
				return x




def regulaFalsi(a, b):
	if f(a) * f(b) > 0:
		print("no")
		return -1

	i = 0
	while math.fabs(b - a) > precizie and i < Nmax:
		i = i + 1
		c =  b - ((f(b) * (b - a)) / (f(b) - f(a)))

		if math.fabs(f(c)) < precizie:
			a = c
			b = c
			return c
		elif f(c) * f(a) < 0:
			b = c
		elif f(c) * f(a) > 0:
			a = c
	
	return c



def metodaSecantei(a, b):
	if f(a) * f(b) > 0:
		print("no")
		return -1

	# c =  b - ((f(b) * (b - a)) / (f(b) - f(a)))	
	c = b - (f(b) * (b - a) / (f(b) - f(a)))
	# x2 = c
	i = 0
	while (math.fabs(f(c)) > precizie) and i < Nmax:
		i = i + 1
		c = b - (f(b) * (b - a) / (f(b) - f(a)))		
		a = b
		b = c
	
	return c



def metodaCoardei(a, b):
	if f(a) * f(b) > 0:
		print("no")
		return -1
	
	c = b
	while math.fabs(b - a) >= precizie:
		c = a - ((b - a) * f(a)) / (f(b) - f(a))
		if math.fabs(f(c)) < precizie:
			return c
		elif f(c) * f(a) < 0:
			b = c
		else:
			a = c
	







def main():
	output = open("solutii.txt", "w")

	x1 = -1
	x2 = 0
	output.write("-------- Metoda bisectiei ----------\n")
	output.write("Singura radacina negativa    %.8f   valoarea functiei = %.8f\n" % (metodaBisectiei(x1, x2), f(metodaBisectiei(x1, x2))))
	
	x1 = 0
	x2 = 1
	output.write("Cea mai mica radacina pozitiva      %.8f  valoarea functiei = %.8f\n" % (metodaBisectiei(x1, x2), f(metodaBisectiei(x1, x2))))

	for x2 in range(1, 21):
		x1 = x2 - 1
		if x2 < 11:
			output.write("A %ia radacina pozitiva      %.8f\n  valoarea functiei = %.8f" % (x2, metodaBisectiei(x1, x2), f(metodaBisectiei(x1, x2))))
		else:
			output.write("A %ia radacina pozitiva     %.8f  valoarea functiei %.8f\n" % (x2, metodaBisectiei(x1, x2), f(metodaBisectiei(x1, x2))))
		output.write("-----------------------------------------------\n")
	output.write("----------------------------------------------------------------\n")


	
	
	output.write("\n\n\n")    	
	output.write("-------- Metoda Newton ----------\n")	
   	
	solutii_metoda_newton = []
	for x in range(-6, 23):
		solutii_metoda_newton.append(int(metodaNewton(x) * math.pow(10, 8)))
   	
	set_solutii_metoda_newton = set(solutii_metoda_newton)
	solutii_metoda_newton = []
	for element in set_solutii_metoda_newton:
		z = element * math.pow(10, -8)
		solutii_metoda_newton.append(z)
	solutii_metoda_newton.sort()

	output.write("Singura radacina negativa     %.8f\n  valoarea functiei = %.8f" % (solutii_metoda_newton[0], f(solutii_metoda_newton[0])))
	output.write("Cea mai mica radacina pozitiva     %.8f  valoarea functiei = %.8f\n" % (solutii_metoda_newton[1], f(solutii_metoda_newton[1])))
	
	for i in range(1, 21):
		output.write("A %ia radacina pozitiva       %.8f  valoarea functiei = %.8f\n" % (i, solutii_metoda_newton[i], f(solutii_metoda_newton[i])))
		output.write("-----------------------------------------------\n")
	
	output.write("----------------------------------------------------------------\n")

	
	



	output.write("\n\n\n")    	
	output.write("-------- Regula Falsi sau Metoda falsei pozitii ----------\n")
	x1 = -1
	x2 = 0
	output.write("Singura radacina negativa    %.8f  valoarea functiei = %.8f\n" % (regulaFalsi(x1, x2), f(regulaFalsi(x1, x2))))
	
	x1 = 0
	x2 = 1
	output.write("Cea mai mica radacina pozitiva      %.8f\n  valoarea functiei = %.8f" % (regulaFalsi(x1, x2), f(regulaFalsi(x1, x2))))

	for x2 in range(1, 21):
		x1 = x2 - 1
		if x2 < 11:
			output.write("A %ia radacina pozitiva       %.8f   valoarea functiei = %.8f\n" % (x2, regulaFalsi(x1, x2), f(regulaFalsi(x1, x2))) )
		else:
			output.write("A %ia radacina pozitiva     %.8f valoarea functiei = %.8f\n" % (x2, regulaFalsi(x1, x2), f(regulaFalsi(x1, x2))) )
		output.write("-----------------------------------------------\n")
	output.write("----------------------------------------------------------------\n")
		





	output.write("\n\n\n")
	output.write("-------- Metoda secantei  ----------\n")
	x1 = -1
	x2 = 0
	output.write("Singura radacina negativa    %.8f  valoarea functiei = %.8f\n" % (metodaSecantei(x1, x2), f(metodaSecantei(x1, x2))))
	
	x1 = 0
	x2 = 1
	output.write("Cea mai mica radacina pozitiva      %.8f valoarea functiei = %.8f\n" % (metodaSecantei(x1, x2), f(metodaSecantei(x1, x2))))

	for x2 in range(1, 21):
		x1 = x2 - 1
		if x2 < 11:
			output.write("A %ia radacina pozitiva       %.8f valoarea functiei = %.8f\n" % (x2, metodaSecantei(x1, x2), f(metodaSecantei(x1, x2))) )
		else:
			output.write("A %ia radacina pozitiva     %.8f  valoarea functiei = %.8f\n" % (x2, metodaSecantei(x1, x2), f(metodaSecantei(x1, x2))) )
		output.write("-----------------------------------------------\n")
	output.write("----------------------------------------------------------------\n")
		

	

	
	output.write("\n\n\n")
	output.write("-------- Metoda coardei  ----------\n")
	x1 = -1
	x2 = 0
	output.write("Singura radacina negativa    %.8f  valoarea functiei = %.8f\n" % (metodaCoardei(x1, x2), f(metodaCoardei(x1, x2))))
	
	x1 = 0
	x2 = 1
	output.write("Cea mai mica radacina pozitiva      %.8f   valoarea functiei = %.8f\n" % (metodaCoardei(x1, x2), f(metodaCoardei(x1, x2))))

	for x2 in range(1, 21):
		x1 = x2 - 1
		if x2 < 11:
			output.write("A %ia radacina pozitiva       %.8f  valoarea functiei = %.8f\n" % (x2, metodaCoardei(x1, x2), f(metodaCoardei(x1, x2))) )
		else:
			output.write("A %ia radacina pozitiva     %.8f\n valoarea functiei = %.8f\n" % (x2, metodaCoardei(x1, x2), f(metodaCoardei(x1, x2))) )
		output.write("-----------------------------------------------\n")
	output.write("----------------------------------------------------------------\n")
	





	output.close()


if __name__ == "__main__":
	main()

