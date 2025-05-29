nota100 = 0
nota50 = 0
nota20 = 0
nota10 = 0
nota1 = 0
valor = 0
saque = int(input('Qual o valor que deseja Sacar: '))
verificar = saque
if verificar > 100:
    if saque > 100:
        nota100 = saque // 100
        valor = saque % 100
        
    if valor > 50:
        nota50 = valor // 50
        valor = valor % 50

    if valor > 20:
        nota20 = valor // 20
        valor = valor % 20  

    if valor > 10:
        nota10 = valor // 10
        valor = valor % 10

    if valor > 1:
        nota1 = valor // 1
        
if verificar < 100:
    if saque > 50:
        nota50 = saque // 50
        valor = saque % 50

    if valor > 20:
        nota20 = valor // 20
        valor = valor % 20  

    if valor > 10:
        nota10 = valor // 10
        valor = valor % 10

    if valor > 1:
        nota1 = valor // 1

if verificar < 50:
    if saque > 20:
        nota20 = saque // 20
        valor = saque % 20  

    if valor > 10:
        nota10 = valor // 10
        valor = valor % 10

    if valor > 1:
        nota1 = valor // 1
        
if verificar < 20:
    if saque > 10:
        nota10 = saque // 10
        valor = saque % 10

    if valor > 1:
        nota1 = valor // 1

if verificar < 10:
    if saque > 1:
        nota1 = saque // 1
    

print(f'O valor vai ser dividido em \n{nota100} notas de R$ 100 \n{nota50} notas de R$ 50 \n{nota20} notas de R$ 20 \n{nota10} notas de R$ 10 \n{nota1} notas de R$ 1')
    


# if saque > 20:
#     print(f'O valor vai ser dividido em \n{nota20} notas de R$ 20 \n{nota10} notas de R$ 10 \n{nota1} notas de R$ 1')
    
# if saque > 10:
#     print(f'O valor vai ser dividido em \n{nota10} notas de R$ 10 \n{nota1} notas de R$ 1')
    
# if saque > 1:
#     print(f'O valor vai ser dividido em \n{nota1} notas de R$ 1')   
    
     
# else:
#     print('O valor é invalido ')
#     print('Só é possivel sacar notas de 100, 50, 20 e 10')


