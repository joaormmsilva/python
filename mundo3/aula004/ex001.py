# def soma(a, b):
#     s = a + b
#     print(f'a soma de {a} + {b} é {s}')
    
    
# soma(10, 12)
# soma(2, 20)
# soma(15, 20)

def contador(*num):
    print(num)

contador(2,1,6)
contador(5,2,1,5)
contador(2,1,6,2,6)

def dobra(lst):
    pos = 0
    while pos <len(lst):
        lst[pos]*=2
        pos+=1
    print(lst)

valor = [5,6,4,1,2,3,5]
print(valor)
dobra(valor)

