from time import sleep
def contador(inicio,fim,passo):
    print(f'Contagem de {inicio} ate {fim} indo de {passo} em {passo}')
    if inicio < fim:
        while inicio <= fim:
            print(inicio, end=' ',flush=True)
            inicio+=passo
            sleep(0.5)
    else:
        while inicio > fim:
            print(inicio, end=' ')
            inicio-=passo
    print('FIM!')


contador(10,0,1)
contador(0,10,1)


inicio = int(input('Qual o inicio'))
fim = int(input('Digite o final: '))
passo = int(input('De quanto em quanto?'))

contador(inicio, fim, passo)