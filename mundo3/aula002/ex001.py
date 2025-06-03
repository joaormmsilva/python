# teste = []
# galera = []

# teste.append('gustavo')
# teste.append(40)

# galera.append(teste[:])
# teste[0] = 'maria'
# teste[1] = 22
# galera.append(teste[:])
# print(galera)


# galera = [['joao', 19],['ana', 33],['bruno', 10],['pedro', 27]]
# idade = 0

# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idaide')
    
    
galera = []
dado = []
totmai = totmen = 0
for cont in range(0,3):
    dado.append(str(input('nome: ')))
    dado.append(int(input('idade: ')))
    galera.append(dado[:])
    dado.clear()
   
for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idaide')
        totmen += 1
        
print(f'temos {totmai} maiores de idadei e {totmen} menores de idade')
