#Solicitar al usuario que ingrese su dirección de correo electrónico. 
# Imprimir un mensaje indicando si la dirección es válida o no, 
# valiéndose de una función para decidirlo. Una dirección se considerará válida si contiene el símbolo "@".


def validar(email):
    validar= correo.count("@")
    if validar==1:
        return True
    return False

correo=input('Introduce tu email, por favor. Tenga en cuenta que debe llevar un @: ')
if validar(correo):
    print('Su dirección de correo electrónico es correcta')
else:
    print=('su direccion de correo electronic es invalida. Por favor, esta vez ingrese un @: ')
    
    




