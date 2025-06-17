par = 0
for c in range(0,7):
    if c % 2 == 0:
        par += c
        print(c, end=' ')
        
print(" ")
print("O valor da soma dos numero é {}".format(par))