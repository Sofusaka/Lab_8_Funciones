#Solicitar al usuario que ingrese un número entero e informarle si es primo o no, 
# utiliza en el código una función booleana que lo decida.

cond="si"
def primo(num):
   for i in range(2,num):
       if num%i==0:           
           return False
   return True
while cond == "si":
    numero=int(input("ingrese un Número para definir si es primo o no: "))
    if primo(numero):
        print("Es primo")
    else:
        print("No es primo")
    cond=input("¿quieres ingresar otro Número? ")
    if cond.lower == "no":
        print("hasta luego, vuelva pronto.")

