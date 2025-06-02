numeros = []
while True:
    pos = 1
    num = int(input(f'digite o {pos} valore'))
    pos += 1
    numeros.append(num)
    verif = input('Quer contuniar [S/N]: ').lower().strip()
    if verif == 'n':
        break
    
print(f'A quantia de numeros digitador foi {len(numeros)}')

numeros.sort(reverse=True)

print(f'os numeros em ordem decrescente fica {numeros}')

if 5 in numeros:
    print('O valor 5 foi entrecontado na lista')
else:
    print('O valor 5 não foi encrontrado na lista')