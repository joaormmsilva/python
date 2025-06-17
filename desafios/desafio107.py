from uteis import numeros

num = float(input('Qual valor voce quer: R$'))
porMais = int(input('Qual porcentagem quer para aumentar: '))
porMenos = int(input('Qual porcentagem quer para diminuir: '))

dobro = numeros.dobrar(num)
metade = numeros.metade(num)
aumentar = numeros.aumentar(porMais, num)
diminuir = numeros.diminuir(porMenos, num)

print(f'O dobro de R${num:.2f} é: R${dobro:.2f}')
print(f'A metade de R${num:.2f} é: R${metade:.2f}')
print(f'O aumento de {porMais}% em R${num:.2f} é igual a R${aumentar:.2f}')
print(f'A redução de {porMenos}% em R${num:.2f} é igual a R${diminuir:.2f}')