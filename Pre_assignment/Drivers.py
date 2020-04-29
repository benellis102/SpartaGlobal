from Pre_assignment.Cars import Car


class Driver:

    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def full_name(self):
        return '{} {}'.format(self.fname, self.lname)

    def person_age(self):
        return '{} is {}'.format(self.full_name(), self.age)

    def owner(self, car):
        return '{} drives {}'.format(Driver.full_name(self), Car.summary(car))
