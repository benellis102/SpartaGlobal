# name = input('please enter your name ')
# age = input('please enter your year of birth ')
# age = (2020 - int(age))
# address = input('please enter your address')
#
# print('are the following details correct?', 'Name:', name, ',', 'Age:', age,  ',', 'Address:', address)
#
# a = 24
# b = 16
# print(a - b)
# print(a + b)
# print(4 * 'me')
# print(8 % 3)
#
# floatnum = 4.3
# intnum = 2
# name = 'bob'
# print(floatnum + intnum)
# print(name + str(floatnum))
#
# example = 'my name jeff'
# print(example.upper())
# print(example)
# print(example.replace('my', 'your'))
#
# a = True
# b = False
# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)
#
# hi = 'Hello World!'
# print(hi.isalpha())
# print(hi.islower())
# print(hi.isupper())
# print(hi.endswith('!'))
# print(hi.startswith('H'))
#
# x = -1
# y = 2
# print(bool(x))
# print(bool(y))
# print(bool(None))
#
# x = input("please enter a word ")
# y = reversed(x)
#
# if list(x) == list(y):
#     print("It is a palindrome")
# else:
#     print('It is Not a palindrome')
#
# shopping_list = ['eggs', 'bread', 'bananas', 'biscuits', 'milk']
# print(shopping_list[2])
# shopping_list[1] = 'roti'
# shopping_list.pop(-2)
# print(shopping_list)
#
#
# x = input('please insert a number')
# y = input('please insert another number')
#
# if int(x) > 5 and int(y) > 15:
#     print('Both are correct')
#
#
# elif int(x) > 5 or int(y) > 15:
#     if int(x) > 5 and int(y) < 15:
#         print('y is incorrect')
#     else:
#         print('x is incorrect')
#
#
# elif not(int(x) > 5 and int(y) > 15):
#     print('Both are incorrect')
#
#
# a = input('Please insert a number ')
# b = input('Please insert another number')
#
# if int(a) > int(b):
#     print('{} is greater'.format(a))
# elif int(a) < int(b):
#     print('{} is greater'.format(b))
# else:
#     print('They are the same')
#
# #
# x = input('Please insert a number ')
# y = input('Please insert a second number ')
# z = input('Please insert a third number')
#
# if int(x) > int(y) and int(x) > int(z):
#     print('{} is the Greatest'.format(x))
# elif int(y) > int(x) and int(y) > int(z):
#     print('{} is the greatest'.format(y))
# elif int(z) > int(x) and int(z) > int(y):
#     print('{} is the greatest'.format(z))
#
# elif int(x) == int(y) or int(x) == int(z):
#     if int(y) > int(x) and int(y) == int(z):
#         print('Y and Z are the same')
#     elif int(x) > int(y) and int(x) == int(z):
#         print('X and Z are the same')
#     else:
#         print('X and Y are the same')
#
# list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_list = []
# for num in list_data:
#     if num < 5:
#         new_list.append(num)
#     else:
#         continue
#
# print(new_list)
#
# white_space = "             hello guys             "
# print(len(white_space))
# print(len(white_space.strip()))
#
# LISTS
# list_data = [10,111,24,56,78,65,80]
# even_list = []
# odd_list = []
# for num in list_data:
#     if num % 2 == 0:
#         even_list.append(num)
#     elif num % 2 != 0:
#         odd_list.append(num)
#     else:
#         continue
# print(even_list)
# print(odd_list)
#
# TUPLES
# essentials = ("Bread", "Eggs", "Milk")
# print(essentials)
# print(essentials.count("Bread"))
#
# DICTIONARY
# students_1 = {
#     "name": "Susan",
#     "stream": "Tech",
#     "completed_lessons": 4,
#     "completed_lessons_names": ["variables", "data_types", "set up"]
# }
# print(students_1["name"])
# print(students_1["stream"])
# print(students_1["completed_lessons_names"][2])
#
# # TUPLES
# car_parts = {"wheels", "doors", "exhaust"}
# car_parts.add("windows")
# print(car_parts)
#
# #CONTROL FLOW
# age = 19
# if age < 19:
#     print('You are not eligible to watch this film')
# else:
#     print('You are good to go')
#
# film_rating = input('Please enter a film rating: ')
#
# if film_rating.lower() == "u":
#     print('All ages are welcome')
# elif film_rating.lower() == 'pg':
#     print('Appropriate for all ages with parental guidance')
# elif film_rating.lower() == '12':
#     print('Appropriate for people over the age of 12')
# elif film_rating.lower() == '12a':
#     print('appropriate for people over the age of 12 with parental guidance')
# elif film_rating.lower() == '15':
#     print('Appropriate for people over the age of 15')
# elif film_rating.lower() == '18':
#     print('Appropriate for people over the age of 18')
# else:
#     print('In correct rating please try again'),
#
# num = input('please insert a number ')
# for i in num:
#     if int(num) % 3 == 0 and int(num) % 5 == 0:
#         print("Fizzbuzz")
#     elif int(num) % 3 == 0:
#         print("Fizz")
#     elif int(num) % 5 == 0:
#         print("Buzz")
#     else:
#         continue
#
# adj = ['red', 'big', 'tasty']
# fruits = ['apple', 'pears', 'cherries']
# taste = ['yum', 'wow', 'woah']
# for x in adj:
#     for y in fruits:
#         for z in taste:
#             print(x, y,z)
#
# list_data = [1,2,3,4,5]
# embedded_list = [[1,2,3],[4,5,6]]
# for data in embedded_list:
#     print(data)
#     for num in data:
#         print(num)
#
# dict_data = {1: {"name": 'Bronson', 'money': '£0.05'}, 2: {"name": 'Masha', 'money': '£3.66'},
#              3: {"name": 'Roscoe', 'money': '£1.14'}}
# x = 0
# while x < 10:
#     print(f"its working --> {x}")
#     x = x + 1
#     if x == 4:
#         break
#
#
