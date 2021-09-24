def sumaDigitos(numero): 
    suma=0 
    while numero !=0:  
        digito=numero%10 
        suma=suma+digito 
        numero=numero//10 
    return suma 
sumatoria=0 
num=int(input("Número a procesar,ingrese 0 para terminar: ")) 
while num!=0: 
    print("Suma:",sumaDigitos(num)) 
    sumatoria+=num 
    num=int(input("Número a procesar,ingrese 0 para terminar: ")) 
print("Sumatoria de los numeros ingresados:", sumatoria) 
print("Suma de los dígitos de la sumatoria:", sumaDigitos(sumatoria))
print('El proceso ha facilitado')
