times = []
cont = 0
while cont <= 20:
    time = input('valores: ')
    times.append(time)
    cont +=1
    print(times)

primeiros = times[0:5]
print(primeiros)
ultimos = times[-5:]
print(ultimos)

ordem = sorted(times)
print(ordem)

chapeco = times.index('chapecoence')
print(chapeco)