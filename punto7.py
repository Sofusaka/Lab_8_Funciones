#Escribir un programa que pida números positivos al usuario. Mostrar el número cuya sumatoria de dígitos fue mayor y 
# la cantidad de números cuya sumatoria de dígitos fue menor que 10. 
# Utilizar una o más funciones, según sea necesario.

cond="si"
def sumaDigitos(numero):
  suma=0
  while numero!=0:
      digito=numero%10
      suma=+digito
      numero=numero//10
  return suma
##############################
cantidad=0
mayor=-1
numero=int(input("Por favor, ingrese un número positivo para averiguar la sumatoria de sus digitos: "))
while cond=="si":
    if numero>=0:
        while numero>=0:
            suma=sumaDigitos(numero)
            if suma > mayor:
                mayor=suma
                n_mayorsuma=numero
            if suma < 10:
                cantidad+=1
            print("La sumatoria de los dígitos de",n_mayorsuma,": ",mayor)
            print("Cantidad de números cuya sumatoria de digitos fue menor a 10: ",cantidad)
            cond=input("¿quiere ingresar otro valor? Escriba si o no ")
            numero=int(input("Por favor, ingrese un número positivo para averiguar la sumatoria de sus digitos:"))
    else:
        print("el numero ingresado es incorrecto")
        cond=="si"
 