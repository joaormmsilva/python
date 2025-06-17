pessoa = {}
grupo = []
idades = []
mulheres = []
cont = 0
while True:
    pessoa['nome'] = str(input('Digite seu nome: '))
    pessoa['sexo'] = str(input('digite seu sexo[M/F]: ')).lower().strip()
    
    while pessoa['sexo'] not in ['m', 'f']:
        print('ERRO! Digite apenas M ou F.')
        pessoa['sexo'] = input('Digite seu sexo [M/F]: ').strip().lower()
        
    pessoa['idade'] = int(input('Digite sua idade: '))
    
    if pessoa['sexo'] == 'f':
        mulheres.append(pessoa.copy())
    
    grupo.append(pessoa.copy())
    veri = input('Quer continuar? [S/N]:  ').lower().strip()
    
    
    if veri in 'nN':
        break
    
while cont < len(grupo):
    idades.append(grupo[cont]['idade'])
    cont += 1

totidade = sum(idades)
mediaIdade = totidade / len(idades)

print('-'*30)
if len(grupo) != 1:
    print(f'- foram informado os dados de {len(grupo)} pessoas')
else:
    print(f'- Foi digitado os dados de 1 pessoa')
    
print(f'- A media de idade do grupo {mediaIdade:.2f}')


print('- do sexo feminino foi colocado: ', end='')
for c in range(len(mulheres)):
    if len(mulheres) > 1:
        print(f'{mulheres[c]['nome']} ', end=' ')
    else:
        print(f'{mulheres[c]['nome']}')
print('')

print(f'- No grupo foi colado de pessoa(s) acima da media: ')
for c in range(len(grupo)):
    if grupo[c]['idade'] > mediaIdade:
        print(f'Nome = {grupo[c]['nome'].title():^5}; Sexo:{grupo[c]['sexo'].upper():^5}; Idade = {grupo[c]['idade']:^5}')
        
print('<<<<<Encerrado>>>>>')