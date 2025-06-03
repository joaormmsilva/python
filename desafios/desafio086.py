matriz = [[],[],[]]
pares = []

for l in range(3):
    for c in range(3):
        num = int(input(f'Digite um número para [{l}, {c}]: '))
        matriz[l].append(num)
        if num % 2 == 0:
            pares.append(num)
        
print('-=' * 15)
for linha in matriz:
    for num in linha:
        soma = sum(linha)
        print(f'[{num:^5}]', end='')
    print()
    
soma = sum(pares)

print(soma)
    
valores = matriz[0][2] +matriz[1][2]+matriz[2][2]
print(valores)
    
maior = max(matriz[1])
print(maior)