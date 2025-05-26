sexo = input('informe seu sexo: (m/f) ').strip().lower()[0]
while sexo not in 'mf':
    sexo = input('dados invalidos digite um sexo valido: ').strip().lower()[0]
print(sexo) 
    