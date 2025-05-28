num = 0 
contador = 0
soma = []


while num != 999:
    num = int(input('Digite um numero, para sair digite 999: '))
    if num != 999:
        print(num)

        soma.append(num)
    else:
        print('\nfim'.upper())
    contador += 1
somar = sum(soma) 
print('Você digitou {} numero antes de 999'.format(contador-1))
print('Os valores colocados sao {} e a somar entre eles é {}'.format(soma,somar))
