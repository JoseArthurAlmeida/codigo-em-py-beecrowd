valor1, valor2, valor3 = map(float, input().split(' '))

# verificando a existencia de um triangulo
def validaTriangulo(a, b, c):
    if ((a + b) > c) and ((a + c) > b) and ((b + c) > a):
        return True
    else:
        return False

if validaTriangulo(valor1, valor2, valor3):
    perimetro = valor1 + valor2 + valor3
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((valor1 + valor2) * valor3) / 2
    print(f"Area = {area:.1f}")