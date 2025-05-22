frase = "Curso em video Python"
frase2 = "Aprenda Python"
print(frase)
print(frase2)
#fatiamento
print(frase[9])      #escreve o 9
print(frase[9:13])   #começa no 9 vai ate o 13
print(frase[9:21])   #começa no 9 vai ate o 21
print(frase[9:21:2]) #começa no 9 vai ate o 21 pulando de 2 em 2
print(frase[:5])     #inicio ate o 5
print(frase[15:])    #15 ate o final
print(frase[9::3])   #vai no 9 ate o final pulando de 3 em 3

#analise
print(len(frase)) #olha o tamanho da frase escrita
print(frase.count('o',0,13)) #mostra quantos tem da palavara escrita entre uma posição e a outra
print(frase.find('deo')) #achar uma frase se achar aparece a posição da primeira letra
print(frase.find('Android')) #achar uma frase se nao existir = -1
print("Curso" in frase) #verificar se tem frase


#transformação
frase.replace('Python','Android') #faz com que troque uma palavra por outra
print(frase.replace('Python','Android'))

frase.upper() #faz com que tudo fique em maiusculo 
print(frase.upper())

frase.lower() #faz com que tudo fique em minusculo
print(frase.lower())

frase.capitalize() #faz com que apenas a primeira letra fique maiusculo
print(frase.capitalize())

frase.title() #faz com que apenas as primeiras letras fiquem em maiusculo
print(frase.title())

frase2.strip #tira os espaços inuteis 
print(frase2.strip())

frase2.rstrip #tira os espaços inuteis da direita(reft)
print(frase2.strip())

frase2.lstrip #tira os espaços inuteis da esquerda(left)
print(frase2.strip())

#divisão
frase.split() #separa as palavras entre espaços formando um array
print(frase.split())

#junção
'-'.join(frase) # junta as palavras pelo caracter colocado no incio
print('-'.join(frase))





