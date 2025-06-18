from math import factorial

def fat(n):
    fatorial = factorial(n)
    return fatorial


numero = int(input('Digite um numero: '))
res = fat(numero)

print(f'O fatorial de {numero} é {res}')