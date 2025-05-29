verificar = 0
total = 0
compra = []
maior = 0
compraMaior = []
menor = 10**100
while True:
    print('-'*40)
    nome = str(input("digite o nome do produto: "))
    preço = float(input("Valor do produto: "))
    print('-'*40)
    produto = nome,preço
    compra.append(nome)
    total += preço
    
    if menor > preço:
        menor = preço
        nomeProduto = nome
    
    if preço > 1000:
        maior += 1
        compraMaior.append(nome)
    
    if verificar == 0:
        verificar = int(input('quer continuar?\n[0]continuar\n[1]parar\nSua opção '))

    if verificar != 0:
        print('-'*40)
        break

print(f'A sua tiveram os produto(s) {compra} e o valor total foi de {total:.2f}\n')
print(f'Voce compro {maior} produto(s) que tem  valor maior que 1000 e o nome desse(s) produto(s) é {compraMaior}\n')
print(f'O produto com menor valor é {menor} e o seu nome é {nomeProduto}\n')