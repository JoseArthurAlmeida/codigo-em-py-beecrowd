nome = input()
salario = float(input())
vendas = float(input())

total = vendas * (15/100) + salario

print(f"TOTAL = R$ {total:.2f}")