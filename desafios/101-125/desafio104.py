def leiaInt(msg):
    while True:
        valor = input(msg)
        if valor.isnumeric():
            return int(valor)
        else:
            print('\033[31mErro! Digite um número inteiro válido.\033[m')


# Programa principal
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')