n1 = int(input('Primira nota: '))
n3 = int(input('Segunda nota: '))
n2 = int(input('Terceira nota: '))

res = (n1 + n2 + n3) / 3

if res < 5:
    print('Você esta reprovado')
elif res >= 5 and res < 7:
    print('Você esta de recuperação')
elif res >= 7:
    print('Voce esta aprovado')