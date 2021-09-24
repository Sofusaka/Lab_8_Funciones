def sumaDigitos(numero):
	suma=0
	while numero !=0:
	    digito=numero%10
	    suma+=digito
	    numero=numero//10
	return suma
num=int(input("Número a procesar, si quiere finalizar ingrese el numero 0: "))
while num!=0:
	print("Suma:",sumaDigitos(num))
	num=int(input("Número a procesar, si quiere finalizar ingrese el numero 0: "))
print('El proceso ha finalizado')
