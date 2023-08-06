# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.


element = int(input("Введите первый элемент прогрессии: "))
delta = int(input("Введите разность: "))
num = int(input("Введите количество элементов: "))


def arithmetic_progression(element, delta, num):
    progression = [element + (i - 1) * delta for i in range(1, num + 1)]
    return progression

print("Арифметическая прогрессия:")
for element in arithmetic_progression(element, delta, num):
    print(element) 

# Если элементы массива выводить в строчку через запятую, то будет так:
# print("Арифметическая прогрессия:")
# print(", ".join(str(element) for element in arithmetic_progression(element, delta, num)))