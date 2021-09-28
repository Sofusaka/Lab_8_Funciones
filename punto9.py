#Escribir una función que, dado un número de cédula de ciudadanía, 
# retorne True si el número es válido y False si no lo es. Consulta cuál es la longitud válida para cédula en Colombia. 

cond="si"
def frecuencia(numero):
   cantidad=0
   while numero!=0:
       ultDigito=numero%10
       cantidad+=1
       numero=numero//10
   return cantidad
while cond=="si":
    num=int(input("ingrese el numero de su cedula de ciudadania: "))
    if frecuencia(num)==10:
        print('el numero ingresado es válido')
    else:
        print('El numero ingresado es invalido')
    
    cond=input("¿quieres volver a ingresar?= ¿si o no? ")
    if cond =="no":
        print('El programa ha finalizado')
