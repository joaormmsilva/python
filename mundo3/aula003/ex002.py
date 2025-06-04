pessoa = {'nome':'João', 'sexo':'M', 'idade': 22}
del pessoa['sexo']
pessoa ['nome'] = 'leandro'
pessoa ['peso'] = '98.5'

print(F'O {pessoa['nome']} tem {pessoa['idade']} anos')
print(pessoa.values())
print(pessoa.keys())

for k, v in pessoa.items():
    print(f'{k} = {v}')
