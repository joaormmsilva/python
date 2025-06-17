num = int(input('Digite um número: '))
tot = 0

for c in range(1, num + 1):
    if num % c == 0:
        tot += 1

if tot == 2:
    print(f'O número {num} é PRIMO.')
    print('O numero {} é divisivel por {} numeros'.format(num,tot))
else:
    print(f'O número {num} NÃO é primo.')
    print('O numero {} é divisivel por {} numeros'.format(num,tot))