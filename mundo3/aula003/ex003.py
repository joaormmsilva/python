# brasil = []
# estado1 = {'UF':'Rio de Janeiro', 'sigla':'RJ'}
# estado2 = {'UF':'São paulo', 'sigla':'SP'}

# brasil.append(estado1)
# brasil.append(estado2)

# print(brasil[0].values())
# print(brasil[1].keys())


estado = {}
brasil = []
for c in range(0,3):
    estado['uf'] = input('Unidade federativa: ')
    estado['sigla'] = input('sigla do estado: ')
    estado['DDD'] = int(input('DDD'))
    brasil.append(estado.copy())
      
for e in brasil:
    for k, v in e.items():
        print(f'o campo {k} tem valor {v}')
