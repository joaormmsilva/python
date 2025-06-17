def ficha(nome, gols):
    if nome == '' and gols == '':
        gols = '0'
        print(f'O jogador <Desconhecido> fez {gols} gols(s) no campeonato')
    elif nome == '':
        print(f'O jogador <Desconhecido> fez {gols} gols(s) no campeonato')
    elif gols == '':
        gols = '0'
        print(f'O jogador {nome} fez {gols} gols(s) no campeonato')
    else:
        print(f'O jogador {nome} fez {gols} gols(s) no campeonato')
        
    
nome = input('nome do jogadro: ').strip()
gols = input('Numero de gols: ').strip()

resultado = ficha(nome,gols)
