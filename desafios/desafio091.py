from random import randint
from time import sleep
jogadores = []
jogador = {}
for c in range(4):
    jogador ['nome']= input(f'Digite seu nome jogador n{c+1}: ')
    jogador ['dado']= randint(1,6)
    jogadores.append(jogador.copy())
    
print('\nValores sorteados:')
for j in jogadores:
    print(f'{j["nome"]} tirou {j["dado"]} no dado.')
    sleep(1)

ranking = sorted(jogadores, key=lambda x: x['dado'], reverse=True)

print('\n🏆 Ranking dos jogadores:')
for i, j in enumerate(ranking):
    print(f'{i+1}º lugar: {j["nome"]} com {j["dado"]}')

