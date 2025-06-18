def numero(n):
    for c in range(n):
        letra = alfabeto[c]
        resposta.append(letra)
        
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']       
resposta = []

numero(int(input("Escolha o numero da letra que quer: ")))

    
print(resposta)