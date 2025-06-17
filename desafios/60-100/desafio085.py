numeros = [[],[]]

for n in range(7):
    num = (int(input(f'Digite o {n+1} numero: ')))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
    

numeros[0].sort()
numeros[1].sort()
print('-='*25)
print(f'Os valores pares digitador foram: {numeros[0]}')
print(f'Os valores impares digitads foram: {numeros[1]}')
