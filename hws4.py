def list_create(n: int) -> list:
    # '''Ф-я принимает на вход целое число n - размер списка
    # Оператор заполняет список натуральными числами
    # Печатает список и возвращает его'''

    list_of_numbers = list(range(0, n))
    i = 0
    while i < n:
        list_of_numbers[i] = int(input(f'Введите {i}-й элемент списка = '))
        i += 1
    print(list_of_numbers)
    return list_of_numbers


def prost_del(n: int) -> list:
    prost_del = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,\
    127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241,251,257,263,\
        269,271,277,281,283,293,307,311,313,317,331,337,347,349,353,359,367,373,379,383,389,397,401,409,419,421,\
            431,433,439,443,449,457,461,463,467,479,487,491,499,503]
    prost_delit = []
    i = 0
    while i < n:
        if n % prost_del[i] == 0:
            prost_delit.append(prost_del[i])
            n = n / prost_del[i]
        else:
            i += 1
    return prost_delit


def no_repeat_elem (li: list) -> list:
    end_list = list()
    end_list.append(li[0])
    i = 1
    while i < len(li):
        if li[i] in end_list:
            i += 1
        else:
            end_list.append(li[i])
            i += 1

    print(li, ' - > ', end_list)


def cript_message(message: str, key: int) -> str:
    # ... Ф принимает на вход сообщение в виде str
    #     Смещает каждый символ сообщения на ключ
    #     Возвращает полученную строку
    # ...
    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    out = ''
    for i in message:
        mesto = alfavit_RU.find(i)   
        new_mesto = mesto + key
        if i in alfavit_RU:
            out += alfavit_RU[new_mesto]
        else:
            out += i
    with open('code.txt', 'w', encoding='utf-8') as code:
        code.writelines(out)

def decrypt_message(key: int) -> str:
    with open('code.txt', 'r', encoding='utf-8') as code:
        code_messege = code.read()
    alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    out = ''
    for i in code_messege:
        mesto = alfavit_RU.find(i)    
        new_mesto = mesto - key    # Меняем знак + на знак -
        if i in alfavit_RU:
            out += alfavit_RU[new_mesto]
        else:
            out += i
    print(out)


def rle_encode(data): # алгоритм кодировки RLE
    encoding = ''
    prev_char = '' 
    count = 1
    if not data: 
        return '' 
    for char in data:  
        if char != prev_char: 
            if prev_char: 
                encoding += str(count) + prev_char 
            count = 1 
            prev_char = char 
        else: 
            count += 1 
    else:  
        encoding += str(count) + prev_char 
     
    return encoding
   

def rle_decode(data: str): # алгоритм декодировки RLE
    decode = '' 
    count = '' 
    for char in data:  
        if char.isdigit(): 
            count += char 
            
        else:              
            decode += char * int(count) 
            count = '' 
    return decode


# 1 - Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]


# n = int(input('Введите натуральное число n (от 2 до 500) = '))

# no_repeat_elem(prost_del(n))


# 2 - Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#  Не использовать множества.
# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]

# my_list = [2, 1, 1, 1, 2, 5, 2, 3, 6, 3, 4]
# end_list = list()
# end_list.append(my_list[0])
# i = 1
# while i < len(my_list):
#     if my_list[i] in end_list:
#         i += 1
#     else:
#         end_list.append(my_list[i])
#         i += 1

# print(my_list, ' - > ', end_list)


# 3 - В файле, содержащем фамилии студентов и их оценки, изменить на прописные буквы фамилии тех студентов, которые имеют средний балл более «4».
# Нужно перезаписать файл.
# Пример:
# Ангела Меркель 5
# Андрей Валетов 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# Программа выдаст:
# АНГЕЛА МЕРКЕЛЬ 5
# АНДРЕЙ ВАЛЕТОВ 5
# Фредди Меркури 3
# Анастасия Пономарева 4

# students = ['Ангела Меркель: 5', 'Андрей Валетов: 5',
#             'Фредди Меркури: 3', 'Анастасия Пономарёва: 4']

# data = open('hws4.txt', 'w', encoding='utf-8') # записываем в файл исходный список
# i = 0
# while i < len(students):
#     data.writelines(students[i])
#     data.write('\n')
#     i += 1
# data.close()


# i = 0 # проверяем на отличников и переводим ФИО в верхний регистр
# while i < len(students):
#     index = int(students[i].find('5'))
#     if index > 0:
#         students[i] = students[i].upper()
#     i += 1
# print(index)
# print(students)

# with open('hws4.txt', 'a', encoding='utf-8') as data: # перезаписываем файл с позициями в верхнем регистре
#     data.write('\n')
#     for i in students:
#         data.writelines(i)
#         data.write('\n')


# 4 - Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество 
# символов влево или вправо. При расшифровке происходит обратная операция. К примеру, слово "абба" 
# можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, а также функцию, которая 
# спрашивает ключ, считывает текст и дешифровывает его.

# key = int(input('Введите ключ: '))
# message = input("Введите текст сообщения: ").upper()

# cript_message(message, key)

# key = int(input('Введите ключ для расшифровки: '))
# decrypt_message(key)




# 5 - Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# файл первый:
# AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool
# файл второй:
# сжатый текст.

# with open('data_in.txt', 'w') as datain:
#     datain.writelines('AAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCDDDDDDEEEEEFFFFG python is sooooooo coooooool')

# with open('data_in.txt', 'r') as datain:
#     data_in1 = datain.read()

# data_code = rle_encode(data_in1)

# with open('data_code.txt', 'w') as data_code1:
#         data_code1.writelines(data_code)


# print(data_code) 
# print(rle_decode(data_code))