nome = input('digit seu nome: ')
nome = nome.lower()

if nome.find('a') == 0:
    print('Seu nome começa com a')
else:
    print('seu nome é '+ nome)