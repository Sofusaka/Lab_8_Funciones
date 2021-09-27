#6.Escribir un programa que pida números al usuario, mostrar la factorial de cada uno y, al finalizar, 
# la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.

cond='si'
def factorial(numero):
   f=1
   if numero!=0:
       for i in range(1,numero+1):
           f=f*i
   return f
cantidad=0
while cond=='si':
    num=int(input("ingrese un Número para obtener su factorial: "))
    print("Factorial:", factorial(num))
    cantidad+=1
    cond=input("¿quieres ingresar otro numero para analizar su factorial? responder si o no: ")
    if cond=='no':
        print("Se leyeron ",cantidad," números ingresados ")
