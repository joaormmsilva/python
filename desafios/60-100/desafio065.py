num = 0
numero = []
contador = 0
limite = int(input("Escreve um limite para finalizer a media: "))

while limite != 0:
    while contador != limite:
        num = int(input("Digite o valor: "))
        numero.append(num)
        contador += 1
    limite = int(input('Voce quer continuar digitando mais valores? caso não digite 0: '))
    contador = 0
    
numero.sort()
media = sum(numero) / len(numero)
somar = sum(numero)

print('os valores são {} e a soma deles é {} \nA media entre todos os numero são {}'.format(numero, somar, media))
print('o menor numero digitado foi {} e o maior numero digitado foi {}'.format(numero[0], numero[-1]))