n1 = float(input('digite a primeira nota: '))
n2 = float(input('digite a primeira nota: '))
m = (n1+n2) / 2

if m >= 6:
    print('sua media é boa')
else:
    print('sua media foi ruim')
print('sua media foi {:.1f}'.format(m))