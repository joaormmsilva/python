from random import randint
from time import sleep

def maior(*num):
    print('-' * 30)
    print('Analisando os valores gerados...')
    sleep(1)
    for n in num:
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print(f'\nForam informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}')
    print('-' * 30)

# Gerando lista com quantidade aleatória de números
numeros = []
aleatorio = randint(1, 10)
for _ in range(aleatorio):
    numeros.append(randint(0, 10))

# Chamando a função usando unpacking (*)
maior(*numeros)
