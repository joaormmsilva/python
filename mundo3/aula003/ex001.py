dados = {'nome':'pedro', 'idade':25}

print(dados['idade'])
dados['sexo'] = 'M'
del dados['idade']
print(dados['sexo'])

filmes= {
    'titulo':'starwar',
    'ano':'1977',
    'diretor':'george'
}

print(filmes.values())
print(filmes.keys())
print(filmes.items())
