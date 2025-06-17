jogador = {}
gols = []
cont = 0


jogador['nome'] = input('Coloque o nome do jogador: ')
partidas = int(input(f'Digite o numero de partidas que {jogador['nome']} jogou: '))
while cont < partidas:
    numero = int(input(f'Qual a quantia de gols feitos na {cont+1} partida por {jogador['nome']}: '))
    if gols != 999:
        gols.append(numero)
    else:
        break
    cont +=1

jogador['gols'] = gols
totgols = sum(gols)
jogador['totgols'] = totgols


print('-'*60)
print(jogador)
print('-'*60)

print(f'O nome do jogador é {jogador['nome']}')
print(f'O jogador {jogador['nome']} fez {jogador['gols']} gols')
print(f'Somando todos os gols feitos pelo jogador {jogador['nome']} foi igual a {jogador['totgols']}')
print('-'*60)

print(f'O jogador {jogador['nome']} jogou {partidas} partidas')
for i,c in enumerate(gols):
    print(f' => na partida {i+1}, fez {c}')
print(f'Foi um total de {jogador['totgols']} gols')