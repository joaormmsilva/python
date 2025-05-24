idades = []
for c in range(7):
    idade = int(input("digite sua idade: "))
    if(idade < 18):
        idades.append(idade)
    
idades.sort()
print('Existem {} pessoas menores de idade as idades são {}'.format(len(idades), idades))