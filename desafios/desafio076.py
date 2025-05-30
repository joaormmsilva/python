nomeP = []
valorP = []

verificar = 1
while True:
    nome = input('Qual o nome do produto: ')
    valor = float(input('Qual o valor: '))
    nomeP.append(nome)
    valorP.append(valor)
    verificar = int(input('''tem mais algum produto 
[0]não
[1]sim'''))
    if verificar == 0:
        break


print('-'*30)
print('LISTA DE PREÇOS'.center(30))
print('-'*30)

for i in range(len(nomeP)):
    print(f'{nomeP[i]:.<20} R$ {valorP[i]:.2f}')

print('-'*30)
print('FIM'.center(30))
print('-'*30)