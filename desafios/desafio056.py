somaidade = 0
mediaidade = 0
maiorHomem = 0
nomeVelho = ' '
totmulher20 = 0

for p in range(1, 5):
    nome = input("Qual seu nome: ")
    sexo = input("Qual seu sexo (masculino ou feminino): ").lower()
    idade = int(input("Qual a sua idade: "))
    somaidade += idade
    if p == 1 and sexo == "m":
        maiorHomem = idade
        nomeVelho = nome
    if sexo == "m" and idade > maiorHomem:
        maiorHomem == idade
        nomeVelho = nome
    if sexo == "f" and idade < 20:
        totmulher20 += 1
        
mediaidade = somaidade / 4
print(totmulher20)
print(maiorHomem)
print(mediaidade)