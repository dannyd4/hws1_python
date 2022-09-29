from calendar import c
import datetime
from pickle import TUPLE1
from random import randint, random
from re import M
import sys


# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

# print('абвгдейка - это передача')

# input_data = 'абвгдейка - это передача'

# input_data1 = input_data.split(' ')

# sub = 'абв'
# output_data = [i for i in input_data1 if not sub in i]
# print('[' + input_data+ ']' + ' ->  ' + " ".join(output_data))


# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета(или сколько вы зададите).
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет(или сколько вы зададите).
# Тот, кто берет последнюю конфету - проиграл.
# Предусмотрите последний ход, ибо там конфет остается меньше.

# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"


# print('Игра конфеты!')

# print('Выбор режима игры: \nИгрок1 vs Игрок2  -  нажмете 1(ввод)\nИгрок1 vs Бот  -  нажмите 2(ввод) ')
# mode = int(input())
# candy_amount = 200


# print()
# print(f'Всего у нас {candy_amount} конфет, игрок может взять от 1 до 28 конфет за ход.\nИгрок, взявший последнюю конфету, проиграл.')
# print()

# print('Жеребьёвка!') # определение очерёдности хода
# hod = randint(1, 11)
# print()


# if hod <= 5:
#     print('Первым ходит игрок1')
#     hod = 1
# else:
#     print('Первым ходит игрок2')
#     hod = 2

# if mode ==1:
#     while candy_amount >= 1: # цикл подсчёта общего кол-ва конфет
#         if hod == 1:
#             candy1 = int(input('игрок1 взял 2- '))
#             if 0 < candy1 < 29:
#                 candy_amount = candy_amount - candy1
#                 if candy_amount < 1:
#                     print('игрок1 - проиграл!')
#                     quit()
#                 print('Осталось конфет: ', candy_amount)
#                 hod = 2
#         if hod == 2:
#             candy2 = int(input('игрок2 взял - '))
#             if 0 < candy2 < 29:
#                 candy_amount = candy_amount - candy2
#                 if candy_amount < 1:
#                     print('игрок2 - проиграл!')
#                     quit()
#                 print('Осталось конфет: ', candy_amount)
#                 hod = 1
# else:
#     while candy_amount >= 1:
#         if hod == 1:
#             candy1 = int(input('игрок1 взял -  '))
#             if 0 < candy1 < 29:
#                 candy_amount = candy_amount - candy1
#                 if candy_amount < 1:
#                     print('игрок1 - проиграл!')
#                     quit()
#                 print('Осталось конфет: ', candy_amount)
#                 hod = 2
#         if hod == 2:
#             candy2 = (candy_amount - 30) % 29
#             if candy2 == 0:
#                 candy2 = randint(1, 29)
#             if candy_amount <= 29:
#                 candy2 = candy_amount-1
#             if 0 < candy2 < 29:
#                 candy_amount = candy_amount - candy2
#                 print('бот взял - ', candy2)
#                 if candy_amount < 1:
#                     print('бот - проиграл!')
#                     quit()
#                 print('Осталось конфет: ', candy_amount)
#                 hod = 1


# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка, написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым она в паре в кортеже,
#  то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите в этой таблице,
# в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком
# https://dzen.ru/media/simplichka/kak-tekst-hranitsia-v-kompiutere-chast-3-62d3d91515d67a522f78e1e6?&





# def tuple(languages: list) -> tuple:
#     '''
#     вход список из строк
#     выход кортеж с порядковыми номерами начиная с 1 (первая позиция в кортеже) и элементами входного списка
#     '''
#     numbers = list(range(1, len(languages)+1))
#     languages1 = [x.upper() for x in languages]
#     tuple1 = list(zip(numbers, languages1))
#     return tuple1


# def filter_tuple(my_tuple: list) -> list:

#     '''
#     вход кортеж с порядковыми номерами начиная с 1 (первая позиция в кортеже) и строк названий языков программирования
#     выход кортеж с фильтром как в задании
#     '''

#     numbers1 = list(range(len(my_tuple)))
#     languages1 = list(range(len(my_tuple)))
#     i = 0
#     sum = 0
#     out_list_languages = []
#     out_list_numbers = []
#     while i < len(my_tuple):
#         numbers1[i], _ = my_tuple[i]
#         _ , languages1[i] = my_tuple[i]
        
#         li = [char for char in languages1[i]]
#         sum = 0
#         for j in li:
#             sum += ord(j)
#         if sum % (i+1) == 0:
#             out_list_languages.append(languages1[i])
#             out_list_numbers.append(sum)
#         i += 1
#     out_list = list(zip(out_list_numbers, out_list_languages))

#     return out_list



# languages = ['Rust','python', 'c#', 'c', 'c++', 'Java', 'javaScript', 'R', 'Arduino', 'Go', 'Swift', 'Matlab', 'Ada']

# tuple1 = tuple(languages)

# print(filter_tuple(tuple1))





 
     
 



