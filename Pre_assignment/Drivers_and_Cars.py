from Pre_assignment.Cars import Car
from Pre_assignment.Drivers import Driver

driver_1 = Driver('Ben', 'Ellis', 21)
driver_2 = Driver('Louis', 'Smith', 22)
driver_3 = Driver('Alex', 'Chatfield', 22)
driver_4 = Driver('Louise', 'Ellis', 55)

car_1 = Car('VW', 'Polo', '1L', 3, 'Hatchback', '60mpg', '100mph', '59bhp', 'Petrol')
car_2 = Car('VW', 'Golf', '1.4L', 5, 'Hatchback', '40mpg', '127mph', '138bhp', 'Petrol')
car_3 = Car('BMW', '2 Series Active Tourer', '2L', 5, 'Hatchback', '50mpg', '130mph', '200bhp', 'Diesel')
car_4 = Car('BMW', '3 Series', '3L', 5, 'Saloon', '23mpg', '155mph', '255bhp', 'Petrol')
car_5 = Car('BMW', '6 Series', '4.8L', 3, 'Coupe', '18mpg', '155mph', '360bhp', 'Petrol')
car_6 = Car('Jaguar', 'XKR', '5L', 3, 'Coupe', '15mpg', '155mph', '500bhp', 'Petrol')
car_7 = Car('Citroen', 'C1', '1L', 3, 'Hatchback', '60mpg', '90mph', '40bhp', 'Petrol')
car_8 = Car('Audi', 'A5', '3.2L', 3, 'Coupe', '30mpg', '155mph', '270bhp', 'Petrol')


vw = [car_1.make_and_model(), car_2.make_and_model()]
bmw = [car_3.make_and_model(), car_4.make_and_model(), car_5.make_and_model()]
jaguar = [car_6.make_and_model()]
citroen = [car_7.make_and_model()]
Audi = [car_8.make_and_model()]
