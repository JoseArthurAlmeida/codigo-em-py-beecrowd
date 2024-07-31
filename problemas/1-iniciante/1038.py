codigo, quantidade = map(int, input().split(' '))

def totalLanche(cod, qtd):
    if(cod == 1):
        return qtd * 4
    elif(cod == 2):
        return qtd * 4.5
    elif(cod == 3):
        return qtd * 5
    elif(cod == 4):
        return qtd * 2
    else: return qtd * 1.5

print(f'Total: R$ {totalLanche(codigo, quantidade):.2f}')
    