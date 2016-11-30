from vehicle import Vehicle

class Car(Vehicle):
    """A class tha models a simple car"""

    def printMe(self):
        speedString = str(self.currentSpeed) + ' miles an hour'
        gearString = {0: 'p',
                      1:'first',
                      2: 'second'}[self.gear] + ' gear'

        print "I am a " + self.make + ' travelling at ' + speedString + " in " + gearString


if __name__ == '__main__':
    ford = Car("ford", 15)
    ford.printMe()
    ford.changeGear(2)
    ford.accelerate(10)
    ford.printMe()
