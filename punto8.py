#Solicitar al usuario el ingreso de números primos. La lectura finalizará cuando ingrese un número que no sea primo.
# Por cada número, mostrar la suma de sus dígitos.
#También solicitar al usuario un dígito e informar la cantidad de veces que aparece en el número (frecuencia).
#Al finalizar el programa, mostrar el factorial del mayor número ingresado.
cond='si'
def primo(num): #Definicion de numero primo
   for i in range(2,num): 
       if num%i==0:            
           return False 
   return True 


def frecuencia(numero,digito): #Definicion de la cantidad de veces que aparece un numero en otro
   cantidad=0 
   while numero!=0: 
       ultDigito=numero%10 
       if ultDigito==digito: 
           cantidad+=1 
       numero=numero//10 
   return cantidad 


def factorial(numero): #Calcular el factorial
   f=1 
   if numero!=0: 
       for i in range(1,numero+1): 
           f=f*i 
   return f 


def sumaDigitos(numero): #La suma de los digitos
  suma=0 
  while numero!=0: 
      digito=numero%10 
      suma=suma+digito 
      numero=numero//10 
  return suma 
mayor=-1 

##Empieza el programa##
while cond == "si": 
    numero=int(input("Ingrese un número primo: ")) 
    while primo(numero): 
        digito=int(input("Dígito: ")) 
        print("Suma de los dígitos:",sumaDigitos(numero)) 
        print("El",digito,"aparece",frecuencia(numero,digito),"veces") 
        if numero > mayor: 
            mayor=numero 
        break 
    else: 
        print("Factorial de",mayor,":",factorial(mayor)) 
        print("El últmo número ingresado no es primo.") 
        print("El programa ha finalizado con éxito") 
        break 
    cond = input("¿Quiere ingresar otro número? si o no = ") 
    if cond == "no": 
        print("Factorial de ",mayor,":",factorial(mayor)) 
        print("El programa ha finalizado con éxito.") 
        break 
