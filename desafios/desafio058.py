import random
numero = random.randint(0, 10)
escolha = int(input('Eu vou escolher um numero entre 0 e 10\nEscolha algum numero para ver se acerta, Voce tera 5 tentativas\nNumero: '))
if escolha > numero:
        print('O numero que escolheu é maior')
if escolha < numero:
    print('o numero que vc escolheu é menor')
tentativas = 0


while escolha != numero:
    escolha = int(input('\nEscolha outro numero'))
    if escolha > numero:
        print('O numero que escolheu é maior')
    if escolha < numero:
        print('o numero que vc escolheu é menor')
    tentativas += 1
    


print('\nVocê Acertou o numero que eu escolhi foi {}. PARABENSS'.format(numero))
print('Voce precisou de {} tentativas para acertar'.format(tentativas))
