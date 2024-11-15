tipoCha = input()
respostas = input().split(" ")

numeroRespostaCorreta = 0

for resposta in respostas:
    if tipoCha == resposta:
        numeroRespostaCorreta += 1

print(numeroRespostaCorreta)