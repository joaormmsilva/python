frase = input('Digite uma frase: ').strip().lower()
frase_sem_espaco = frase.replace(' ', '')
inverso = frase_sem_espaco[::-1]

if frase_sem_espaco == inverso:
    print('É um PALÍNDROMO!')
else:
    print('NÃO é um palíndromo.')