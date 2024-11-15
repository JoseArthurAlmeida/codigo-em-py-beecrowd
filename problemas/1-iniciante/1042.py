listaInteiros = list(map(int, input().split(" ")))

listaCrescente = sorted(listaInteiros)

print("\n".join(map(str, listaCrescente)) + "\n")
print("\n".join(map(str, listaInteiros)))