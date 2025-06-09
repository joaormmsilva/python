def contador(i,f,p):
    """
    -> faz uma comtagem e mostra na tela.
    :param i: Inicio da comtagem
    :param f: Fim da contagem
    :param p: Passo da comtagem
    :return: Sem retorno
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c+=p
    print('fim')  
    
    

help(contador)