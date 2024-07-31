valor = int(input())

print(valor)

notas = [100, 50, 20, 10, 5, 2, 1]

for nota in notas:
    qtdNotas = int(valor / nota)
    valor%=nota
    print(f"{qtdNotas} nota(s) de R$ {nota},00")