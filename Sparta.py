# name = input('please enter your name ')
# age = input('please enter your year of birth ')
# age = (2020 - int(age))
# address = input('please enter your address')
#
# print('are the following details correct?', 'name:', name, ',', 'age:', age,  ',', 'address:', address)

# a = 24
# b = 16
# print(a - b)
# print(a + b)
# print(4 * 'me')
# print(8 % 3)

# floatnum = 4.3
# intnum = 2
# name = 'bob'
# print(floatnum + intnum)
# print(name + str(floatnum))

# example = 'my name jeff'
# print(example.upper())
# print(example)
# print(example.replace('my', 'your'))

# a = True
# b = False
# print(a == b)
# print(a != b)
# print(a >= b)
# print(a <= b)

# hi = 'Hello World!'
# print(hi.isalpha())
# print(hi.islower())
# print(hi.isupper())
# print(hi.endswith('!'))
# print(hi.startswith('H'))

# x = -1
# y = 2
# print(bool(x))
# print(bool(y))
# print(bool(None))

# x = "radar"
# y = reversed(x)
#
# if list(x) == list(y):
#     print("Is a palindrome")
# else:
#     print('Not a palindrome')

# shopping_list = ['eggs', 'bread', 'bananas', 'biscuits', 'milk']
# print(shopping_list[2])
# shopping_list[1] = 'roti'
# shopping_list.pop(-2)
# print(shopping_list)

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


# a = input('Please insert a number ')
# b = input('Please insert another number')
#
# if int(a) > int(b):
#     print('{} is greater'.format(a))
# elif int(a) < int(b):
#     print('{} is greater'.format(b))
# else:
#     print('They are the same')


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
# elif int(x) == int(y) or int(x) == int(z):
#     if int(y) > int(x) and int(y) == int(z):
#         print('Y and Z are the same')
#     elif int(x) > int(y) and int(x) == int(z):
#         print('X and Z are the same')
#     else:
#         print('X and Y are the same')

list_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for num in list_data:
    if num < 5:
        new_list.append(num)
    else:
        continue

print(new_list)
