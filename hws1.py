# Домашнее задание к 1 семинару

# 1. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет,
# является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет

# a = int(input('Введите число от 1 до 7 - '))

# if a == 6 or a == 7:
#     print('- ',a,' -> да')

# else:
#     print('- ',a,' -> нет')


# 2 Задача. Напишите программу для. проверки истинности утверждения
#  ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

# def test_bit(data, offset):
#     mask = 1 << offset
#     return data & mask

# a = 0b000
# while a < 9 :

#     if (not(test_bit(a, 0) or test_bit(a, 1) or test_bit(a, 2)) == (not(test_bit(a, 0)) and not(test_bit(a, 1)) and not(test_bit(a, 2)))):
#         print(not(test_bit(a, 0) or test_bit(a, 1) or test_bit(a, 2)) == (not(test_bit(a, 0)) and not(test_bit(a, 1)) and not(test_bit(a, 2))))
#         a+=1
#     else:
#         print('Равенство неверно')
#         sys.exit()
# print('Равенство верно')


# 3 Задача. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
#  в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

# x = int(input('Введите координату х не равную 0  - '))
# y = int(input('Введите координату y не равную 0  - '))

# if x == 0 and y == 0:
#     print('Точка находится в центре координат')
# elif x == 0:
#     print('Точка находится на оси у')
# elif y == 0:
#     print('Точка находится на оси x')
# elif x > 0 and y > 0:
#     print('Точка находится в первой четверти')
# elif x < 0 and y > 0:
#     print('Точка находится во второй четверти')
# elif x < 0 and y < 0:
#     print('Точка находится в третьей четверти')
# elif x > 0 and y < 0:
#     print('Точка находится в четвёртой четверти')


# 4 Задача. Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

# x = int(input('Введите номер четверти (1-4)- '))

# if x == 1:
#     print('x и y от 1 до +бесконечность')
# elif x == 2:
#     print('x от -1 до -бесконечность, y от 1 до +бесконечность')
# elif x == 3:
#     print('x от -1 до -бесконечность, y от -1 до -бесконечность')
# elif x == 4:
#     print('x от 1 до +бесконечность, y от -1 до -бесконечность')


# 5 Задача. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

# from math import *
# def distance(x1, y1, x2, y2):
#     c = sqrt((x2-x1)**2 + (y2-y1)**2)

#     print(round(c,3))

# x1 = int(input('Введите координату х1 первой точки  - '))
# y1 = int(input('Введите координату y1 первой точки  - '))
# x2 = int(input('Введите координату х2 второй точки  - '))
# y2 = int(input('Введите координату y2 второй точки  - '))

# distance(x1, y1, x2, y2)