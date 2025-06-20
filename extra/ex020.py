def numero(n):
    for c in range(n):
        letra = alfabeto[c]
        resposta.append(letra)
        
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']       
resposta = []
escolha = int(input("Escolha um numero entre 1 e 26 : "))

if escolha >26:
    print('Numero fora dos paremetros ')
    numero(int(input('Escolha outro numero: ')))
    print(resposta)  
else:
    numero(escolha)
    print(resposta)  
    
