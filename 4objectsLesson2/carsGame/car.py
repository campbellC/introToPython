class Car():
    """A very simple car class - it has gears and a speed"""

    def __init__(self, make, maxSpeed):
        self.make = make
        self.maxSpeed = maxSpeed
        self.gear = 0
        self.currentSpeed = 0

    def changeGear(self, n):
        self.gear = n

    def accelerate(self,n):
        if self.currentSpeed == self.maxSpeed:
            return
        else:
            self.currentSpeed += n

    def printMe(self):
        speedString = str(self.currentSpeed) + " miles an hour"
        gearString = {0: "P",
                      1: "first",
                      2: "second",
                      3: "third",
                      4:'fourth',
                      5: 'fifth'}[self.gear] + " gear"
        print "I am a " + self.make + " travelling at " +speedString+ " in " +gearString

if __name__ == '__main__':
    ford = Car("ford", 15)
    ford.printMe()
    ford.changeGear(5)
    ford.accelerate(10)
    ford.printMe()
