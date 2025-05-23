import random 
from time import sleep

computador = random.choice(['pedra', 'papel', 'tesoura'])
resposta = input('Escolha algum entre pedra, papel ou tesoura: ')

print('Pensando...')
sleep(2)

if computador == 'pedra' and resposta == 'tesoura' or computador == 'tesoura' and resposta == 'papel' or computador == 'papel' and resposta == 'pedra':
    print('\033[31mVoce perdeu para mim\033[m')
    print('Eu escolhi {} e vc escolheu {}'.format(computador, resposta))
elif resposta == 'pedra' and computador == 'tesoura' or resposta == 'tesoura' and computador == 'papel' or resposta == 'papel' and computador == 'pedra':
    print('\033[32mVoce me venceu. Parabens\033[m')
    print('Eu escolhi {} e vc escolheu {}'.format(computador, resposta))
elif resposta == computador:
    print('deu empate')