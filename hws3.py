def sum_odd_list_elements(list1: list) -> int:
# ...
    # Функция принимает на вход список с данными типа: int
    # Возвращает сумму элементов под нечётными индексами
# ...
    i = 1
    sum_odd = 0

    while i < len(list1):
        if i == 1 or i % 2 > 0:
            sum_odd += list1[i]
        i += 1
    return sum_odd


def mult_pair_list_elements(list1) -> list:
# ...
# Функция принимает на вход список с данными типа: int
# Возвращает список с попарным произведением элементов (нулевой-последний, первый-предпоследний...)
# ...
    length_list = len(list1)
    if length_list % 2 == 0:
        mult_list = list(range(length_list//2))
        i = 0
        while i < (length_list/2):
            mult_list[i] = list1[i]*list1[length_list-(1+i)]
            i+=1
        return mult_list
    else:
        mult_list = list(range((length_list//2)+1))
        i = 0
        while i < (length_list//2):
            mult_list[i] = list1[i]*list1[length_list-(1+i)]
            i+=1
        mult_list[i] = list1[i]*list1[i]
        return mult_list


def decimal_parts_max_minus_min(list1) -> float:
# ...
#     Функция принимает на вход список с данными типа: float
#     Возвращает значение разницы между максимальным и минимальным значениями дробных частей элементов списка
# ...
    decimal_parts = list(range(len(list1)))
    i = 0
    max = list1[0] - int(list1[0])
    min = list1[0] - int(list1[0])
    while i < len(list1):
        decimal_parts[i] = round(list1[i] - int(list1[i]), 12)
        if max < decimal_parts[i]:
            max = float(decimal_parts[i])
        if min > decimal_parts[i]:
            min = float(decimal_parts[i])
        i += 1

    return round(max-min, 12)

def dec_bin(x):
# ...
    # Функция принимает на вход число в формате: str
    # Возвращает значение принятого числа в двоичном формате
# ...
    if int(x) == 0:
        return (str(0))
    if int(x) == 1:
        return (str(x))
    else:
        y = str(int(x) % 2)
        return (str(dec_bin(int(x)//2)) + (y))


def fibonachi(k: int) -> list:
    # ...
    #         Ф-я принимает на вход целое положительное число к
    #         Возвращает к элементов последовательности Фибоначи как в плюс, так и в минус
    # ...
        fib_pos = list(range(k+1))
        fib_pos[0] = 0
        fib_pos[1] = 1
        fib_neg = list(range(k))
        i = 2
        while i <= k:
                fib_pos[i] = fib_pos[i-2]+fib_pos[i-1]
                i += 1
        j = 0
        while j < k:
                fib_neg[j] = ((-1)**(j))*fib_pos[j+1]
                j += 1
        fib_neg.reverse()
        fib = fib_neg + fib_pos 
        return fib



# 1- Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

# length_list = int(input('Введите размерность списка (0-10) = '))
# if 10 < length_list < 0:
#     exit()

# list1 = list(range(length_list))
# i = 0
# while i < length_list:
#     list1[i] = int(input(f'Введите {i}-й элемент списка (натуральное число)'))
#     i += 1

# print(list1, 'Сумма чисел под нечётными индексами = ', sum_odd_list_elements(list1))


# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

# length_list = int(input('Введите размерность списка (0-10) = '))
# if 10 < length_list < 0:
#     exit()

# list1 = list(range(length_list))
# i = 0
# while i < length_list:
#     list1[i] = int(input(f'Введите {i}-й элемент списка (натуральное число)')) # заполнение списка значениями
#     i += 1

# print(list1, 'Список с попарным произведением элементов = ', mult_pair_list_elements(list1))


# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91


# length_list = int(input('Введите размерность списка (0-10) = '))
# if 10 < length_list < 0:
#     exit()

# list1 = list(range(length_list))
# i = 0
# while i < length_list:
#     list1[i] = float(input(f'Введите {i}-й элемент списка (вещественное число)'))
#     i += 1

# print(list1, 'Разница между максимальной дробной частью и минимальной',decimal_parts_max_minus_min(list1))


# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10

# x = (input('Введите целое положительное число для перевода в двоичную систему счисления = '))
# print(x, '- в двоичной сист. счисления = ', dec_bin(x))

# 5-Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи


# k = int(input('Введите количество элементов последовательности Фибоначи (0-15) = '))
# if 10 < k < 0:
#     exit()

# print(fibonachi(k))
