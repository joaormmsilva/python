pares = []
impares = []
numeros = []

for n in range(7):
    num = (int(input(f'Digite o {n} numero: ')))
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
        
    
    
numeros.append(pares[:])
numeros.append(impares[:])

numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitador foram: {numeros[0]}')
print(f'Os valores impares digitads foram: {numeros[1]}')