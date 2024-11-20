lista = list(map(int, input().split(' ')))
lista.sort(reverse=True)
a, b = lista

if a % b == 0:
    print("Sao Multiplos")
else: 
    print("Nao sao Multiplos")