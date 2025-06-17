saque = int(input('Qual o valor que deseja sacar? '))

nota100 = saque // 100
resto = saque % 100

nota50 = resto // 50
resto = resto % 50

nota20 = resto // 20
resto = resto % 20

nota10 = resto // 10
resto = resto % 10

nota1 = resto // 1

print(f'O valor vai ser dividido em:')
if nota100 > 0:
    print(f'{nota100} nota(s) de R$ 100')
if nota50 > 0:
    print(f'{nota50} nota(s) de R$ 50')
if nota20 > 0:
    print(f'{nota20} nota(s) de R$ 20')
if nota10 > 0:
    print(f'{nota10} nota(s) de R$ 10')
if nota1 > 0:
    print(f'{nota1} nota(s) de R$ 1')