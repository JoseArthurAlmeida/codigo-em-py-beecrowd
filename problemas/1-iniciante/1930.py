from functools import reduce
reguas = list(map(int, input().split(' ')))

tomadas = reduce(lambda x, y: x + y, reguas)

print(tomadas - 3)