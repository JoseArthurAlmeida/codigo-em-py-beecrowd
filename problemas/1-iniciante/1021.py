valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1.00, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for nota in notas:
    qtdNotas = int(valor / nota)
    valor%=nota
    print(f"{qtdNotas} nota(s) de R$ {nota}.00")
    
print("MOEDAS:")
for moeda in moedas:
    qtdMoedas = int(valor / moeda)
    valor= (valor % moeda) + 0.00001
    print(f"{qtdMoedas} moeda(s) de R$ {moeda:.2f}")