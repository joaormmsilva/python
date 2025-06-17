numeros = []
impar = []
par = []
pos = 1
while True:
    num = int(input(f'digite o {pos} valor: '))
    pos += 1
    numeros.append(num)
    verif = input('Quer contuniar [S/N]: ').lower().strip()
    if verif == 'n':
        break
    

for valor in numeros:
    if valor % 2 == 0:
        par.append(valor)
    else:
        impar.append(valor)

print(f'Todos os numero que digitou foram {numeros}')
print(f'Dentro dessa lista os numeros pares foram {par}')
print(f'E os numeros imapares foram {impar}')