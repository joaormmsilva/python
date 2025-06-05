from datetime import datetime
pessoa = {}

#dados base

pessoa['nome'] = input('Digite seu nome: ')
ano = int(input('Ano de nascimento: '))
ano_atual = datetime.now().year
pessoa['idade'] =  ano_atual - ano
pessoa['carteiraTrabalho'] = int(input('Digite sua Carteira de Trabalho (0 caso não tenha): '))

# ver se pode se aposentar 

if pessoa['carteiraTrabalho'] != 0:
    
    pessoa['contratacao'] = int(input('Digite o ano de contratação: '))
    pessoa['salario'] = int(input('Digite seu salario: '))
    
    pessoa['tempo_contribuicao'] = ano_atual - pessoa['contratacao']
    
    if pessoa['idade'] >= 64 and pessoa['tempo_contribuicao'] >= 35:
        pessoa['situacao'] = 'valido'
        
    elif pessoa['idade'] < 64:
        falta = 64 - pessoa['idade'] 
        pessoa['situacao'] = 'invalido'
   
    elif pessoa['idade'] >= 64 and pessoa['tempo_contribuicao'] < 35:
        falta = 35 - pessoa['tempo_contribuicao']
        pessoa['situacao'] = 'invalido'
       
else:
    pessoa['situacao'] = 'Sem registro'     
    pessoa['tempo_contribuicao'] = 0
        
#mostra as informações

if pessoa['carteiraTrabalho'] != 0:
    print('\nRELATÓRIO FINAL')
    print(f'{"NOME":<12} {"IDADE":^8} {"CTPS":^8} {"CONTRIB.":^10} {"SALARIO":^12} {"SITUAÇÃO":^20}')
    print('-' * 75)
    print(f'{pessoa["nome"]:<12} {pessoa["idade"]:^8} {pessoa["carteiraTrabalho"]:^8} {pessoa["tempo_contribuicao"]:^10} R${pessoa["salario"]:^10.2f} {pessoa["situacao"]:^20}')
else:
    print('\nRELATÓRIO FINAL')
    print(f'{"NOME":<12} {"IDADE":^8} {"SITUAÇÃO":^20}')
    print('-' * 45)
    print(f'{pessoa["nome"]:<12} {pessoa["idade"]:^8} {pessoa["situacao"]:^20}')