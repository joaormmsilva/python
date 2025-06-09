def teste(b):
    global a
    a=8
    b+=4 
    c=2
    print(f'Em teste o b vale {a}')
    print(f'Em teste o b vale {b}')
    print(f'Em teste o b vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')
