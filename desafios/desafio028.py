import random

numero = random.randint(0,5)
resposta = int(input('Adivinhe um numero de 0 a 5: '))

if numero == resposta:
    print('voce acertou')
else:
    print('voce errou o numero')
    
print(numero)
print(resposta)