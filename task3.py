# 3) Сгенерируйте список на 30 элементов. Отсортируйте список по возрастанию,
# методом сортировки выбором.

from random import randint
numbers = []
for i in range(30):
    numbers.append(randint(-10, 10))
print(numbers)

for i in range(29):
    i_min = i
    for j in range(i + 1, 30):
        if numbers[i_min] > numbers[j]:
            i_min = j
            numbers[i], numbers[i_min] = numbers[i_min], numbers[i]
print(numbers)