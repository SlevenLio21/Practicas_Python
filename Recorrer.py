def run():
    nombre = input('Escribe tu nombre : ')
    for letra in nombre:
        print(letra)
    
    frase = input('escribe un caracter : ')
    for caracter in frase:
        print(caracter.upper())

if __name__ == '__main__' :
    run()