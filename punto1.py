
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
    
    




