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