import random

def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero entre el 1 y 100'))
    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('Busca un numero mayor ')
        else:
            print('Busca un numero menor ')
        numero_elegido = int(input('Elige otro numero :'))
    print('Ganaste')



if __name__ == '__main__':
    run()