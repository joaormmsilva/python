from time import sleep
def contador(inicio,fim,passo):
    print(f'Contagem de {inicio} ate {fim} indo de {passo} em {passo}')
    if inicio < fim:
        while inicio < fim+1:
            print(inicio, end=' ')
            inicio+=passo
    else:
        while inicio > fim:
            print(inicio, end=' ')
            inicio-=passo
    print('FIM!')

contador(10,0,1)
contador(0,10,1)

