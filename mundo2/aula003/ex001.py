# for c in range (1,5):
#     n = int(input('digite um valor'))
# print('fim')

# n = 1
# while n != 0:
#     n = int(input('digite um valor'))
#     print(n)
# print('fim')

par = impar = 0
n=1 
while n != 0:
    n = int(input('digite um valor'))
    if n!= 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
            
print(par, impar)
print("acabou")