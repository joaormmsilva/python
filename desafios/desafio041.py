from datetime import date
nascimento = int(input('Escreve seu ano de nascimento'))

ano = date.today().year
idade = ano - nascimento 

if idade <= 9:
    print('Nadador Mirim sua idade é {}'.format(idade))
    
elif idade <= 14 and idade > 9:
    print('Nadados Infantil sua idade é {}'.format(idade))
    
elif idade <= 19 and idade > 14:
    print('Nadados Junior sua idade é {}'.format(idade))
    
elif idade <= 20 and idade > 19:
    print('Nadados Senior sua idade é {}'.format(idade))
    
elif idade > 20:
    print('Nadados Master sua idade é {}'.format(idade))
