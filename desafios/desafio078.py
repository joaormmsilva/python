lista = []

# Ler 5 valores numéricos e guardar na lista
for i in range(5):
    num = int(input(f'Digite o {i+1}º valor: '))
    lista.append(num)

# Encontrar maior e menor
maior = max(lista)
menor = min(lista)

print('-'*40)
print(f'Você digitou os valores: {lista}')
print(f'O maior valor foi {maior} nas posições:', end=' ')
for i, v in enumerate(lista):
    if v == maior:
        print(i, end=' ')

print(f'\nO menor valor foi {menor} nas posições:', end=' ')
for i, v in enumerate(lista):
    if v == menor:
        print(i, end=' ')
