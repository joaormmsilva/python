num = [2,5,9,1]
num[2] = 3
num.insert(0,7)
num.sort(reverse = True)
num.append(10)
num.pop(2)
num.remove(7)
print(num)
print(f'esse lista tem {num} elementos')


valores = [12,3,4,6,23,5,7,987]

# for cont in range(0,11):
#     valores.append(int(input('Digite um valor: ')))

valores.sort()
for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}...')



a = [2,3,4,5,7]
b = a[:]
b[2] = 10
print(f'A lista A: {a}')
print(f'A lista B: {b}')