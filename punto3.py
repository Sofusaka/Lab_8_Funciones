#Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos. 
# Al finalizar, mostrar la sumatoria de todos los números ingresados y la suma de sus dígitos. 
# Reutilizar la misma función realizada en el ejercicio 2.  este no es.

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
