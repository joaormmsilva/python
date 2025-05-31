lanche = ['lanche','suco','pizza','sorvete']
lanche.append('cooki')
lanche.insert(1,'hotdog')

#apagar
del lanche[3]
lanche.pop(0)
lanche.remove('sorvete')
print(lanche)

if 'macarrão' in lanche:
    lanche.remove('macarrão')

valores = list(range(4,11))
valores.sort(reverse=True)

print(valores)

print(len(valores))
