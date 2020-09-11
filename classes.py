class Dog():
    """A simple attempt to model a dog"""

    def __init__(self, name, age):
        """initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(self.name.title() + " rolled over!")


class Car():
    """A simple attempt to represnet a car"""

    def __init__(self, make, model, year):
        """init attributes"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """print a statement showing the car's mileage."""
        print("This cas has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """sets the odometer"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """add the miles to odometer"""
        if miles > 0:
            self.odometer_reading += miles
        else:
            print("You can't reduce mileage!")

class Battery():
    """A battery model for an EV"""

    def __init__(self, battery_size=70):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Batter description"""
        print("This car has a " + str(self.battery_size) + "-kWh battery")

    def get_range(self):
        """Shows the range of the battery"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        message = "This car can go approx. " + str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery(85)


