class Vehicle():
    """A superclass of vehicles
    Implementing very basic vehicle functionality"""

    def __init__(self, make, maxSpeed):
        self.make = make
        self.maxSpeed = maxSpeed
        self.gear = 0
        self.currentSpeed = 0

    def changeGear(self, n):
        self.gear = n

    def accelerate(self, n):
        if self.currentSpeed + n >= self.maxSpeed:
            return
        else:
            self.currentSpeed += n


if __name__ == '__main__':
    print "hi"
