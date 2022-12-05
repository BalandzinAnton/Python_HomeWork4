# 2) Написать программу, которая генерирует двумерный массив на A x B
# элементов ( A и B вводим с клавиатуры)
# И считаем средне-арифметическое каждой строки (не пользуемся встроенными
# методами подсчета суммы)

import random
from random import randint
a = int(input('Введите значение А '))
b = int(input('Введите значение B '))
arr = [[0 for i in range(b)] for j in range(a)]
for i in range(a):
    for j in range(b):
        arr[i][j] = randint(1, 9)

for i in range(a):
    for j in range(b):
        print(arr[i][j], end=' ')
    print()
s = 0
for i in range(a):
    for j in range(b):
        s += arr[i][j]
        result = s / b
    print(f"Среднне аврифметическое строки {i + 1} равно: {result}")
    s = 0