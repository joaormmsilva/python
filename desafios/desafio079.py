posição = 1
valores = []

while True:
    valor = int(input(f'Digite o {posição}° valor: '))
    
    if valor in valores:
        print('Valor duplicado! não vou adicionar...')
    else:
        valores.append(valor)
        print('Valor adicionado com sucesso... ')
        posição +=1
    verif = input('Quer continuar?[S/N] ').lower().strip()
    if verif == 'n':
        break
        
        
valores.sort()
print(valores)