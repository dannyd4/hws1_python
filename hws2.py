# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 
# Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# 0.56 -> 11

# num = input("Введите дробное: ") #разделим введённое (тип данных строка) на две части

# x = num.split(".") 
# print(x)

# a = int(x[0]) # целая часть
# b = int(x[1]) # дробная часть
# if a < 0:
#     a = -(a)
# sum = 0
# while (a != 0): # сумма числа целой части
#     sum = sum + (a % 10)
#     a = a // 10
# while (b != 0): # сумма числа дробной части
#     sum = sum + (b % 10)
#     b = b // 10
# print("Сумма цифр равна:", sum) 





# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Добавьте проверку числа N: чтобы пользователь не мог ввести буквы.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# number_str = int(input('input positive integer value - '))

# mult  = 1
# list1 = list(range(0,number_str))
# i=0
# while i < number_str:
#     list1[i] = mult *(i+1)
#     mult = list1[i]
#     i+=1
# print(list1) 


# 3 - Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.
# Напишите такую программу, которая найдет палиндром введенного пользователем числа


# number_str = (input('input positive integer value from 10 to 99999- ')) 

# number_rev_str = number_str[::-1]

# number_int = int(number_str)

# if int(number_int) < 0:
#      number_int = -(number_int)

# number_rev_int = int(number_rev_str)

# while number_rev_str != number_str:
#     number_int += number_rev_int
#     number_str = str(number_int) 
#     number_rev_str = number_str[::-1]

# print(number_int, ' - палиндром!')


# 4 - Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)

# import datetime


# test = input('Press Enter for generate a random value from 0 to 9999')

# now = datetime.datetime.now()
# random_value = now.microsecond // 100

# print(random_value)
