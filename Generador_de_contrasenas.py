import random

def generar_contrasena():
    mayuscula = ['A' , 'B', 'C', 'D', 'E' , 'F', 'G' ]
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g' ]
    simbolos = ['!', '#', '*', '&', '_' , '@']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    caracteres = mayuscula + minusculas + simbolos + numeros 

    contrasena = []

    for i in range(15):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

        contrasena = " ".join(contrasena)
        return contrasena





def run():
    contrasena = generar_contrasena()
    
    print('nueva contrasena es : ' + contrasena)



if __name__ == '__main__':
    run()