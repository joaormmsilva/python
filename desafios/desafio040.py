n1 = float(input('A primeira nota foi: '))
n2 = float(input('A segunda nota foi: '))
trabalho = float(input('A nota do trabalho foi: '))

media = (n1 + n2 + trabalho) / 3

if media < 5.5:
    print('Voce foi \033[31mREPROVADO\033[m pois sua primeira prova teve a nota {:.1f} a sua segunda prova teve a nota {:.1f} e a nota do seu trabalho foi {:.1f} dando um total de {:.1f} sendo menor que a media para recuperação de 5.5'.format(n1,n2,trabalho,media))
    
elif media >= 5.5 and media <7:
    print('Voce esta de \033[31mRECUPERAÇÂO\033[m pois sua primeira prova teve a nota {:.1f} a sua segunda prova teve a nota {:.1f} e a nota do seu trabalho foi {:.1f} dando um total de {:.1f} sendo o valor menor que media 7'.format(n1,n2,trabalho,media))
    
elif media >= 7 and media <= 9.5:
    print('Voce esta \033[32mAPROVADO\033[m pois sua primeira prova teve a nota {:.1f} a sua segunda prova teve a nota {:.1f} e a nota do seu trabalho foi {:.1f} dando um total de {:.1f} Estando dentro da media 7'.format(n1,n2,trabalho,media))
    
elif media > 9.5:
    print('PARABENS!!. Você esta \033[32mAPROVADO\033[m pois sua primeira prova teve a nota {:.1f} a sua segunda prova teve a nota {:.1f} e a nota do seu trabalho foi {:.1f} dando um total de {:.1f}. Sendo a maior nota que poderia tirar'.format(n1,n2,trabalho,media))   
