import random
from functools import reduce
from math import *

# def list_mult(number: list) -> list:
#     '''
#     Вход: список с натуральными числами
#     Выход: список являющ. попарным произведением 0 эл и последний, 1 эл и предпоследний...
#     '''
#     if N % 2 == 0:
#         out_list = list(map(lambda x, y: x*y, numbers, numbers[::-1]))
#         return out_list[:int(N / 2)]
        
#     else: 
#         out_list = list(map(lambda x, y: x*y, numbers, numbers[::-1]))
#         return out_list[:int((N / 2)+1)]
        
# def poisk_second_enter(my_list: list, my_str: str) -> int:
#     '''
#     вход - проверяемый список и запрос в виде строки
#     выход- индекс второго вхождения запроса или -1 если такового нет
#     '''
#     count = 0
#     for i in range(0, len(my_list)):
#         if my_str == my_list[i]:
#             count += 1 
#             if count == 2:
#                 print('список: ', my_list ,  'ищем:' , my_str , 'ответ: ' , i)
#                 break
#     else:
#         print('список: ', my_list ,  'ищем:' , my_str , 'ответ: -1')
    
# def distance(x1, y1, z1, x2, y2, z2):
#     c = sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

#     print(round(c,3))

# 1- Определить, присутствует ли в заданном списке строк, некоторое число

# while True:
#     try:
#         N = int(input('Введите размерность списка N (от 0 до 1000) = '))
#     except ValueError:
#         print("Вы ввели не число. Попробуйте снова.")
#     else:
#         if 0 <= N < 1001:
#             break

# str1 = int(input('Введите целое число для поиска от 0 до 100  - '))

# numbers = [random.randint(0, 100) for i in range(N)] # заполняем список
# print(numbers)

# count1 = numbers.count(str1)
# print(f'В заданном списке число {str1} встречается {count1} - раз')


# 2- Найти сумму чисел списка стоящих на нечетной позиции

# while True:
#     try:
#         N = int(input('Введите размерность списка N (от 0 до 100) = '))
#     except ValueError:
#         print("Вы ввели не число. Попробуйте снова.")
#     else:
#         if 0 <= N < 101:
#             break

# numbers = [random.randint(0, 100) for i in range(N)] # заполняем список
# print(numbers)

# numbers1 = list(filter(lambda x: x, numbers[1::2])) # фильтруем по нечётным индексам
# print(numbers1, ' -> элементы на нечётных позициях')

# numbers2 = reduce(lambda x, y: x+y, numbers1) # суммируем элементы
# print(numbers2, ' -> сумма элементов на нечётных позициях')



# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)


# point1 = str(input('Введите координаты первой и второй точки в формате x1 y1 z1 x2 y2 z2 - '))

# point_list = point1.split()

# coordinates = list(map(int, point_list[0:6]))

# distance(coordinates[0], coordinates[1], coordinates[2], coordinates[3], coordinates[4], coordinates[5])


# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

# list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
# str1 = "qwe"

# list2 = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
# str2 = "йцу"

# list3 = ["йцу", "фыв", "ячс", "цук", "йцукен"]
# str3 = "йцу"

# list4 = ["123", "234", 123, "567"]
# str4 = "123"

# list5 = []
# str5 = "123"

# poisk_second_enter(list1, str1)
# poisk_second_enter(list2, str2)
# poisk_second_enter(list3, str3)
# poisk_second_enter(list4, str4)
# poisk_second_enter(list5, str5)

# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# while True:
#     try:
#         N = int(input('Введите размерность списка N (от 0 до 100) = '))
#     except ValueError:
#         print("Вы ввели не число. Попробуйте снова.")
#     else:
#         if 0 <= N < 101:
#             break

# numbers = [random.randint(0, 100) for i in range(N)]
# print(numbers)

# print(list_mult(numbers))



# 6-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# while True:
#     try:
#         N = int(input('Введите размерность последовательности N (от 0 до 100) = '))
#     except ValueError:
#         print("Вы ввели не число. Попробуйте снова.")
#     else:
#         if 0 <= N < 101:
#             break

# my_list  = list(map(lambda x: ((-1)**x)*(3**x), range(0, N)))
# print(my_list)
