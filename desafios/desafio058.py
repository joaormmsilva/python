import random
numero = random.randint(0, 10)
escolha = int(input('Adivinhe o numero que estou pensando: '))
print('\nVoce errou')
print('Eu escolhi o numero {} e você escolheu o numero {}'.format(numero, escolha))


while escolha != numero:
    numero = random.randint(0, 10)
    escolha = int(input('\nEscolha outro numero'))
    print('\nVocê errou\nEu escolhi o numero {} e você escolheu o numero {}'.format(numero, escolha))

        
print('\nVocê Acertou o numero que eu escolhi foi {} e você colocou {}'.format(numero, escolha))
print(' ')
