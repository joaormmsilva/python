palavras = ['macaco', 'macarrão', 'python', 'arroz']

for palavra in palavras:
    print(f'\nNa palavra "{palavra}" temos:', end=' ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
