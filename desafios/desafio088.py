aluno = []
dados = []
nota = []
medias = []

while True:
    dados.append(str(input('digite seu nome: ')))
    nota.append(int(input('Digite a primeira nota: ')))
    nota.append(int(input('Digite a segunda nota: ')))
    
    media = sum(nota)/2
    medias.append(media)
    
    dados.append(nota[:])
    dados.append(medias[:])

    
    aluno.append(dados[:])

    
    ver = input('quer continuar? [s/n]: ').lower()
    if ver == 'n':
        break
    
    medias.clear()
    nota.clear()
    dados.clear()


print('=-'*40)

print(f'No. NOME  Media')
for p, c in enumerataluno)):
    
    print(f'{aluno[c][0]:-^20} \nNa primeira prova {aluno[c][1][0]} \nNa segunda prova {aluno[c][1][1]} \nSua media é {aluno[c][2]}')
    
print(f'{"="*30}')
