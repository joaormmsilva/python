def notas(*num, situacao=False):
    res = {}
    res['total'] = len(num)
    res['maior'] = max(num)
    res['menor'] = min(num)
    res['media'] = sum(num) / len(num)
    
    if situacao:
        if res['media'] >= 7:
            res['situacao'] = 'boa'
        elif res['media'] >= 5:
            res['situação'] = 'Razoável'
        else:
            res['situação'] = 'Ruim'
            
    return res

resultado = notas(5.5, 8.5, 10, 6.5, situacao=True)
print(resultado)

        
