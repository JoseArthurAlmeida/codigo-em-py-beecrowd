segundos = int(input())

horas = int(segundos/3600)
segundos%=3600

minutos = int(segundos/60)
segundos%=60

print(f"{horas}:{minutos}:{segundos}")