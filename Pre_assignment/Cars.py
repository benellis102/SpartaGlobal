class Car:
    def __init__(self, make, model, engine_size, doors, body_type, mpg, top_speed, bhp, fuel):
        self.make = make
        self.model = model
        self.engine_size = engine_size
        self.doors = doors
        self.body_type = body_type
        self.mpg = mpg
        self.top_speed = top_speed
        self.bhp = bhp
        self.fuel = fuel

    def make_and_model(self):
        return '{} {} '.format(self.make, self.model)

    def performance(self):
        return 'With {} it can reach a top speed of {}'.format(self.bhp, self.top_speed)

    def body(self):
        return "The car is a {} with {}doors ".format(self.body_type, self.doors)

    def economy(self):
        return "With a {} {} engine it averages {}".format(self.engine_size, self.fuel, self.mpg)

    def summary(self):
        return "a {} {}, {} {} {} which has {} doors".format(self.engine_size, self.fuel, self.make, self.model,
                                                             self.body_type, self.doors)
