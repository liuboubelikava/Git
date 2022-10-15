# print(5*2)
# user_name = input("Waht's your name")
# print(f'Hello, {user_name}!')
# print('Hello, World!')
# print('*********')
# print('*       *')
# print('*       *')
# print('*********')
# print('*********\n*       *\n*       *\n*********')
# user_name = input("Enter your name")
# age = int(input('Enter your birth year:'))
# current_age = 2022 - age
# message = 'Hello,'
# print('{} {}. your age is: {}'.format(message, user_name, current_age))
# name = input('Enter your name: ')
# for symbol in name:
#     print(f'index {name.index(symbol)} - {symbol}')
# i = 0
# while i < 5:
#     i = i + 1
#     if i == 3:
#         continue
#     print(i)
# age = float(input('Enter your age: '))
# if age < 13:
#     print("Where's your mom?")
# elif age >= 21:
#     print('Welcome!')
# else:
#     print('Go home')
# i = 5
# while i > 0:
#     print(i, 'Hello')
#     i = i - 1
# # print('Go!')
# i = 0
# while i < 5:
#     i = i + 1
#     if i == 3:
#         continue
#     print(i)
# def give_me_power(num, n):
#     return num**n
# print(give_me_power(2, 5))
# print(give_me_power(2, 4))
# x = 2
# if x == 5:
#     print('Five')
# elif x > 5:
#     print('More than five')
# else:
#     print('Less than five')
# name = input('Input your name: ')
# for letter in name:
#     print(letter)
# name = input('Enter your name: ')
# for symbol in name:
#     print(f'index {name.index(symbol)} - {symbol}')
# number = 0
# if number:
#     print('true')
# else:
#     print('false')
# for i in range(5):
#     print(i, 'Hello!')
# for i in range(0, -10, -1):
#     print(i)
# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# x = 5
# if x == 5:
#     print('Five')
# else:
#     print('Not five')
# x = 5
# if x == 5:
#     print('five')
# elif x > 5:
#      print('more than five')
# else:
#     print('less than five')
# i = 0
# while i<5:
#     print('Hello')
#     i = i+1
# i = 1
# while i <= 5:
#     print("Hello")
#     if i == 3:
#         break
#     i = i+1
# i = 1
# while i <= 5:
#     print("Hello")
#     if i == 3:
#         continue
#     i = i+1
# name = input("Enter your name")
# for letter in name:
#     print(letter)
# for i in range(5):
#     print(i)
# name = input("Enter your name")
# for letter in name:
#     print(letter, end = ' ')
# for i in range(1,10,2):
#     print(i)
# for i in range(2,11,2):
# i<=0
# if i>=0:
#     print('true')
# else:
#     print('false')
# Homework 3
# Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# Option 1
# my_list = ['a', 'b', [1,2,3], 'd']
# print(my_list[2][0])
# print(my_list[2][1])
# print(my_list[2][2])
# Option 2
# my_list = ['a', 'b', [1, 2, 3], 'd']
# list1 = my_list[2]
# print(*list1, sep='\n')
# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# #Using lambda and filter
# print(sum(filter(lambda x: isinstance(x, int), list_1)))
# #Using list comprehension
# print([x for x in list_1 if isinstance(x, str) and 'a' in x])
# print(sum([x for x in list_1 if type(x) == int]))
# print ([y for y in list_1 if type(y) == str and "a"in y])
# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
# print(tuple(['cat', 'dog', 'horse', 'cow']))
# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
# family_1 = tuple(input('Введите текст через запятую: ').split(','))
# family_2 = tuple(input('Введите текст через запятую: ').split(','))
# if len(family_1) == len(family_2):
#     print('Equal')
# elif len(family_1) > len(family_2):
#     print('family_1')
# else:
#     print('family_2')
# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение
# film_dictionary = {
#     'title': 'Hachico',
#     'director': 'Lasse Hallstrom',
#     'year': '2010',
#     'budget': '16 million dollars',
#     'main_actor': 'Richard Gere',
#     'slogan': 'True dog story'
# }
# print(film_dictionary.keys())
# print(film_dictionary.values())
# print(film_dictionary.items())
# print(*film_dictionary.keys())
# print(*film_dictionary.values())
# print(*film_dictionary.items())
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# sum_dic = sum(my_dictionary.values())
# print(sum_dic)
# sum_dic = (sum(my_dictionary[item]for item in my_dictionary))
# print(sum_dic)
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# result = 0
# for x in my_dictionary:
#     result += my_dictionary[x]
# print(result)
# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# new_list = set([1, 2, 3, 4, 5, 3, 2, 1])
# print(new_list)
# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
#      - проверьте являются ли эти множества подмножествами друг друга
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set1.symmetric_difference(set2))
# print(set1.issubset(set2))
# print(set2.issubset(set1))
# Homework4
# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# from math import sqrt
# def square (side):
#     return (side * side, side * 4, round(sqrt(side ** 2 * 2)))
# print(square(9))
# def square (storona_kvadrata):
#         perimetr = 4*storona_kvadrata
#         ploshad =2*storona_kvadrata
#         diagonal = (storona_kvadrata*2)+(storona_kvadrata*2)
#         return perimetr, ploshad, diagonal
# print(square(16))

# 4.2.    Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer
# def employee(**kwargs):
#     for k, v in kwargs.items():
#         print(f'{k}: {v}')
#
# employee(last_name='Smith', name='John', age=35, position='web developer')
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# print(list(filter(lambda x: x > 0, my_list)))
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# from functools import reduce
# my_list = [20, -3, 15, 2, -1, -21]
# print(reduce(lambda x, y: x*y, my_list))
# Чтобы получить результат перемножения только положительных значений
# print(reduce(lambda x, y: x*y, [x for x in my_list if x > 0]))
# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
# from My_calc import *
# div_res1 = divide(45, 9)
# print(div_res1)
# div_res2 = divide(5, 0)
# print(div_res2)
# add_res = add(585, 1987)
# print(add_res)
# remain_res = remain(541, 6)
# print(remain_res)
# sub_res subtract(230, 149)
# print(sub_res)
# Homework 5
class Employee:
      def __int__(self, name, surname):
            self.name = name
            self.surname = surname

Employee1 = Employee ("Alex", "Smith")
print(employee1.name)
print(employee1.surname)




