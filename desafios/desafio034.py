salario = float(input("Digite o seu salario: "))
if salario > 1250:
    aumento = salario * 0.10 + salario
    print("Com o o almento do seu salario ele ficou {}".format(aumento))
else:
    aumento = salario * 0.15 + salario
    print("Com o o almento do seu salario ele ficou {}".format(aumento))