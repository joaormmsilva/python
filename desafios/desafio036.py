casa = float(input('qual o valor da casa: '))
salario = float(input('qual o salario mensal: '))
anos = int(input('Em quantos anos planeja pagar: '))

meses = anos * 12

prestacao = casa / meses
limite =salario * 0.30

if prestacao > salario * 0.30:
    print('\033[31m❌ Empréstimo reprovado!\033[m')
    print('A parcela mensal de R${:.2f} excede 30% do seu salário (R${:.2f}).'.format(prestacao, limite))
else:
    print('\033[32m✅ Empréstimo aprovado!\033[m')
    print('A parcela mensal será de R${:.2f} durante {} meses.'.format(prestacao, meses))