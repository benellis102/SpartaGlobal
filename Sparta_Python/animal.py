# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def bark(self):
#         return 'woof'
#
#     def eat(self):
#         return '{} says i am eating chicken'.format(self.name)

# class Person:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#
#     def talk(self):
#         age = input('How old are you?: ')
#         return "{} is {} years old".format(self.fname,age)
#
class Cars:
    def __init__(self, make, model, name):
        self.make = make
        self.model = model
        self.name = name

    def what(self):
        return 'you drive a {}, {}'.format(self.make, self.model)

    def heatedseats(self):
        return 'have you turned on the heated seats'
