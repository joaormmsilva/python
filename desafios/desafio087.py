from random import randint
from time import sleep
palpite = []
jogos = []

quantiJogos = int(input('Quanto jogos quer palpite? '))

for n in range(quantiJogos):
    
    while len(jogos) <= 6:
        num = randint(1,60)
        if num not in jogos:
            jogos.append(num)
        
    jogos.sort()
    palpite.append(jogos[:])
    jogos.clear()

print(f'{"SORTEADOR":=^35}')
for i,jogo in enumerate(palpite):
    print(f'jogo {i+1}: {jogo}')
    sleep(1)
print(f'{"="*40}')
