frase = input('Escreva uma frase: ').lower()
vogal = 0

for i in frase:
    if i in 'aeiou':
        vogal += 1

print(f'a frase "{frase}" tem um total de {vogal} vogais')