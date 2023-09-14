# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

x = int(input('Введите начало диапазона: '))
y = int(input('Введите конец диапазона: '))

lst = list()
lst_1 = list()
for i in range(10):
    lst.append(random.randint(-5, 20))
    if lst[i] >= x and lst[i] <= y:
        lst_1.append(i)

print(lst)
print(lst_1)


