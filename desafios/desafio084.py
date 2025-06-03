pessoa = []
dados = []
pesada = []
leves = []

while True:
    nome = (input('qual seu nome: '))
    peso = int(input('qual seu peso: '))
    dados.append(nome)
    dados.append(peso)
    
    pessoa.append(dados[:])
    if peso >= 100:
        pesada.append(dados[:])
    else:
        leves.append(dados[:])
    dados.clear()
    veri = input('Quer continuar [s/n]: ').lower()
    if veri == 'n':
        break

print('-='*30)    
print(f'Foram cadastradas {len(pessoa)} pessoas')

print('-='*30)  

print(f'tiver {len(pesada)} pessoas com mais de 100.0Kg e foram. ')
for p in pesada:
    print(f'{p[0]} com {p[1]}')
    
print('-='*30)  

print(f'tiver {len(leves)} pessoas com menos de 100.0Kg e foram. ')
for l in leves:
    print(f'{l[0]} com {l[1]}')
    
print('-='*30)  



