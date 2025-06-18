c = 1
mulher = []
pessoa = {}
grupo = []
idades = []

while True:
    print('=-'*20)
    print(f'{f"dados da {c}° pessoa":^40}')
    print('=-'*20)
    
    pessoa['nome'] = input('Nome: ')
    idade = int(input('Idade: '))
    pessoa['idade'] = idade
    pessoa['sexo'] = input('Sexo[f/m]: ').lower()
    
    grupo.append(pessoa.copy())
    idades.append(idade)
    
    if pessoa['sexo'] == 'f':
        mulher.append(pessoa.copy())
        
    c +=1
    veri = input('Quer continuar? [s/n]: ').lower()
    if veri in ['não', 'n', 'nao']:
        break
   
media = sum(idades) / len(idades)
    
print('-'*30)
print(f'O total de pessoas é {len(grupo)}')
print(f'A media das idades é {media:.0f}')

print('as mulheres são', end=': ')
for c in mulher:
    print(c['nome'], end=';')
print('')

print('as pessoas com idade acima da media são', end=': ')
for c in grupo:
    if c['idade'] > media:
        print(c['nome'], end=';')
print('')
print('-'*30)