numeros = [1,2,5,3,7,2,7,24,7,9,56,87,345,123,5,7,5678]

while True:
    numero = int(input('Digite um numero: '))
    
    if numero in numeros:
        print('Esse numero esta na lista')
        break
    else: 
        print('esse numero não esta na liste tente novamente')