expressao = input('Difite uma Expressão: ')

parenteseEsq = expressao.count('(')
parenteseDir = expressao.count(')')
parentese = parenteseDir + parenteseEsq

if parentese % 2 != 0:
    print('a equação esta errada')
else:
    print('Expressão valida')
