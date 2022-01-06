import battery


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


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery(85)
