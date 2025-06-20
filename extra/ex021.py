def somar(n1, n2):
    return n1 + n2

def dividir(n1, n2):
    if n2 == 0:
        print('❌ Erro! Divisão por zero.')
        return None
    return n1 / n2

def subtrair(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def traco():
    print('=-' * 25)

n1 = float(input('Primeiro número: '))
n2 = float(input('Segundo número: '))

while True:
    funcao = int(input('''
----------------------------------
  Escolha qual operação deseja:
----------------------------------
  [0] Somar
  [1] Subtrair
  [2] Multiplicar
  [3] Dividir
----------------------------------
Sua escolha: '''))

    if funcao == 0:
        res = somar(n1, n2)
        traco()
        print(f'O resultado de {n1} + {n2} = {res}')
        traco()
    elif funcao == 1:
        res = subtrair(n1, n2)
        traco()
        print(f'O resultado de {n1} - {n2} = {res}')
        traco()
    elif funcao == 2:
        res = multiplicar(n1, n2)
        traco()
        print(f'O resultado de {n1} X {n2} = {res}')
        traco()
    elif funcao == 3:
        res = dividir(n1, n2)
        if res is not None:
            traco()
            print(f'O resultado de {n1} ÷ {n2} = {res}')
            traco()
    else:
        print('❌ Opção inválida!')

    continuar = input('Quer fazer mais alguma operação? [sim/não]: ').lower()
    if continuar in ['não', 'nao', 'n']:
        print('FIM')
        break
    else:
        escolher = int(input('''
Quer continuar com o resultado anterior ou digitar novos números?
  [0] Continuar com o resultado
  [1] Digitar novos números
Sua escolha: '''))
        traco()
        if escolher == 0:
            n1 = res
            n2 = float(input('Digite o novo segundo número: '))
        else:
            n1 = float(input('Digite o primeiro número: '))
            n2 = float(input('Digite o segundo número: '))
