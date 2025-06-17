numeros = ('zero','um','dois','tres','quatro','cinco','seix','sete','oito','nove','dez','onze','doze','treza','quatorze','quinze','dezeseis',"dezesete",'dezoito','dezenove','vinte')


res = int(input('Digite um numero entre 0 e 20: '))
while res > 20 or res < 0:
    print('invalido')
    res = int(input('Digite um valor valido entre 0 e 20: '))

valor = numeros[res]
print(f'Voce digiteu o numero {valor}')