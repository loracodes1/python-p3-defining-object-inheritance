class Vehicle:
    def __init__(self, wheel_size, wheel_number):
        """
        Initializes a Vehicle instance with wheel size and number.
        """
        self.wheel_size = wheel_size
        self.wheel_number = wheel_number

    def go(self):
        """
        Simulates the vehicle moving.
        """
        return "vrrrrrrrooom!"

    def fill_up_tank(self):
        """
        Simulates filling up the vehicle's tank.
        """
        return "filling up!"


