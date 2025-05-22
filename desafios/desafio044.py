valor = float(input('O valor do produto é: '))
print('''[1] dinheiro
[2] pix
[3] cartão''')
modo = int(input('Qual mode de pagamento prefere: '))


if modo == 1:
    desconto =  valor - valor * 0.05 
    print('O valor do produto com desconto via pix é {:.2f}'.format(desconto))
    
elif modo == 2:
    desconto = valor - valor * 0.10
    print('O valor do produto com desconto via pix é {:.2f}'.format(desconto))
    
elif modo == 3:
     vezes = int(input('''Pode ser pago em ate 3X quantos gostaria: 
    [1] 1x no cartão
    [2] 2x no cartão
    [3] 3x no cartão  '''))
     
     if vezes == 1:
        vezes1 = valor
        print('o valor do produto sera {:.2f}'.format(vezes1))
        
     elif vezes == 2:
        vezes2 = valor * 0.10 + valor
        print('O valor pago via ser {:.2f}'.format(vezes2))
        
     elif vezes == 3:
        vezes3 = valor * 0.20 + valor
        print('O valor pago via ser {:.2f}'.format(vezes3))
        
else:
    print('modo de pagamente não aceito')