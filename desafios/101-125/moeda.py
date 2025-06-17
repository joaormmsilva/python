def aumentar(n, porcentagem):
    return n + (n * porcentagem / 100)

def diminuir(n, porcentagem):
    return n - (n * porcentagem / 100)

def dobro(n):
    return n * 2

def metade(n):
    return n / 2

def moeda(valor):
    return f'R${valor:.2f}'.replace('.', ',')

def resumo(preco, aumento, reducao):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{moeda(dobro(preco))}')
    print(f'Metade do preço: \t{moeda(metade(preco))}')
    print(f'{aumento}% de aumento: \t{moeda(aumentar(preco, aumento))}')
    print(f'{reducao}% de redução: \t{moeda(diminuir(preco, reducao))}')
    print('-' * 30)
