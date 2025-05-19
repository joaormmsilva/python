frase = "Curso em video python"

print(frase[9])      #escreve o 9
print(frase[9:13])   #começa no 9 vai ate o 13
print(frase[9:21])   #começa no 9 vai ate o 21
print(frase[9:21:2]) #começa no 9 vai ate o 21 pulando de 2 em 2
print(frase[:5])     #inicio ate o 5
print(frase[15:])    #15 ate o final
print(frase[9::3])   #vai no 9 ate o final pulando de 3 em 3

print(len(frase))
print(frase.count('o',0,13))
print(frase.find('deo'))