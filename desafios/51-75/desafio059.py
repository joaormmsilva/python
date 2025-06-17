n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

operação = 0
res = 0

while operação == 0:
    print('''
          [1] somar
          [2] subtrair
          [3] multiplicar
          [4] dividir
          [5] trocar numero
          [6] encerrar
          ''')
    opção = int(input('qual sua operação?'))
    if opção == 1:
        res = n1 + n2
        operação = opção
        
    if opção == 2:
        res = n1 - n2
        operação = opção
        
    if opção == 3:
        res = n1 * n2
        operação = opção
        
    if opção == 4:
        res = n1 / n2
        operação = opção
        
    if opção == 5:
        n1 = int(input("Digite o novo valor"))
        n2 = int(input("Digite o novo valor"))
        
    if opção == 6:
        operação = opção
    

if operação == 1:
    print('O resultado de {} + {} é igual a {}'.format(n1,n2,res))
if operação == 2:
    print('O resultado de {} - {} é igual a {}'.format(n1,n2,res))
if operação == 3:
    print('O resultado de {} x {} é igual a {}'.format(n1,n2,res))
if operação == 4:
    print('O resultado de {} / {} é igual a {}'.format(n1,n2,res))       
if operação == 6:
    print('fim do programa') 