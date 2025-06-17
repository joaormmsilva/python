menor18 = 0
homem = 0
quantia = 0
mulherMenor18 = 0
mulher = 0
while True:
    idade = int(input('Qual sua idade: '))
    sexo = str(input("Qual seu sexo: "))
    pessoa = idade,sexo
    quantia += 1
    if idade < 18:
        menor18 +=1
        
    if sexo == 'm' or sexo == 'M' or sexo == 'masculino' or sexo == 'Masculino':
        homem += 1
        
    if sexo == 'f' or sexo == 'F' or sexo == 'feminino' or sexo == 'Feminino':
        mulher += 1
    
    if sexo == 'f' or sexo == 'F' or sexo == 'feminino' or sexo == 'Feminino' and idade < 20:
        mulherMenor18 += 1
    verificar = input('quer continuar? [sim/não]')
    if verificar == 'não' or verificar == 'nao':
        break


if menor18 != 0:
    print(f'A quantia de pessoas que tem a idade menor que 18 é {menor18}')
else:
    print(f'Não tem pessoas menor que 18 anos')

if homem != 0:
    if homem == 1:
        print(f'Dentro das {quantia} pessoas adicionadas apenas 1 é homens')
    else:
        print(f'Dentro das {quantia} pessoas adicionadas {homem} são homens')
else:
    print(f'não teve nenhum homem cadastrado apenas mulheres')
    
if mulherMenor18 != 0:
    print(f'e dentro das {quantia} pessoas adicionadas {mulherMenor18} são mulheres menores que 20 anos')
else:
    print(f'todas as mulheres tem a idade maior que 20 e existem {mulher} mulheres')