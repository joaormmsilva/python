from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando 5 valores: ', end='', flush=True)
    for _ in range(5):
        valor = randint(1, 10)
        lista.append(valor)
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
    print('')

def soma_par(lista):
    soma = sum(num for num in lista if num % 2 == 0)
    print(f'A soma dos valores pares é {soma}')

# Programa principal
numeros = []
sorteia(numeros)
soma_par(numeros)
