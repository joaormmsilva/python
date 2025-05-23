import datetime
nascimento = int(input('Qual seu ano de nascimento: '))
ano = datetime.date.today().year
idade = ano - nascimento 
faltam =  18 - idade 
passou = faltam - faltam*2

if idade <= 17:
    print('\033[31mVocê ainda ira ter que fazer o alistamento militar\033[m')
    print('faltam {} para voce passar pelo alistamento'.format(faltam))
    print(idade)
elif idade == 18:
    print('Esta no ano de se alistar')
    print(idade)
elif idade > 18:
    print('\033[32mVocê passou pelo alistamento militar\033[m')
    print('fazem {} que voce passou pelo alistamento'.format(passou))
    print(idade)