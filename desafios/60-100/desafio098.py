from time import sleep
def contador(inicio,fim,passo):
    print(f'Contagem de {inicio} ate {fim} indo de {passo} em {passo}')
    
    if passo <0:
        p*=-1
    if passo == 0:
        passo = 1
    if inicio < fim:
        while inicio <= fim:
            print(inicio, end=' ',flush=True)
            inicio+=passo
            sleep(0.5)
    else:
        while inicio >= fim:
            print(inicio, end=' ',flush=True)
            inicio-=passo
            sleep(0.5)
    print('FIM!')


contador(1,10,1)
contador(10,0,2)


inicio = int(input('Qual o inicio'))
fim = int(input('Digite o final: '))
passo = int(input('De quanto em quanto?'))

contador(inicio, fim, passo)