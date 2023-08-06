# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Пример использования
# sample_list = [10, 5, 7, 15, 3, 9, 12, 8]
# min_value = 5
# max_value = 12

from random import randint
sample_list = [randint(1, 50) for i in range(1, 11)]
print(sample_list)
min_value = int(input("Введите начало диапазона: "))
max_value = int(input("Введите конец диапазона: "))

def find_indexes_in_range(lst, min_val, max_val):
    indexes = [index for index, value in enumerate(lst) if min_val <= value <= max_val]
    return indexes

result = find_indexes_in_range(sample_list, min_value, max_value)
print("Индексы элементов, принадлежащих заданному диапазону:")
print(result)