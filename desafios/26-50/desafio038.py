num1 = int(input('Escreva o primeiro numero: '))
num2 = int(input('Escreva o segundo numero: '))

if num1 > num2:
    print('O primeiro numero é o maior')
elif num2 > num1:
    print('O segundo numeor é o maior')
elif num1 == num2:
    print('Não existe um valor maior os dois são iguais')