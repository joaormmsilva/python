jogador = {}
gols = []
jogadores = []
while True:
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
     
    jogador['gols'] = gols[:]
    totgols = sum(gols)
    jogador['totgols'] = totgols  
    
    jogadores.append(jogador.copy()) 
    veri = input('quer continuar?: [S/N]').lower()
    gols.clear()  
    if veri == 'n':
        break

print('-' * 50)
print(f'{"cod.":<4} {"NOME":<8} {"gols":>20} {"Total":>10}')
for v, c in enumerate(jogadores):
    print(f'{v:<4} {c["nome"]:<8} {str(c["gols"]):>20} {c["totgols"]:>10}')
print('-' * 50)

while True:
    ver = int(input('Mostar dados de qual jogador[999 para]? '))
    
    if ver == 999:
        print('-' * 50)
        print('Finalizando...')
        print('-' * 50)
        break
    
    if ver >= len(jogadores):
        print('-' * 50)
        print('ERRO! Não existe jogador com código 5! tente novamente')
        print('-' * 50)
    else:
        print(f'-- Levantamento do jogador {jogadores[ver]["nome"]}')
        for i, g in enumerate(jogadores[ver]["gols"]):
            print(f' => No jogo {i + 1} fez {g} gols')
        print('-' * 50)