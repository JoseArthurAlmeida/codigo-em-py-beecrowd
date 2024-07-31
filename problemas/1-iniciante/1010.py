total = 0

for i in range(2): 
    cod, numPeca, valorPeca = input().split(" ")
    total = total + (int(numPeca) * float(valorPeca))

print(f"VALOR A PAGAR: R$ {total:.2f}") 