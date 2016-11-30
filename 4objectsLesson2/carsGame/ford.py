from car import Car

class Ford(Car):
    def printMe(self):
        print "I'm a Ford! I go fast."
        print "I'm going " + str(self.currentSpeed) + " miles an hour."

if __name__ == '__main__':
    ford = Ford("ford", 15)
    ford.printMe()
    ford.changeGear(5)
    ford.accelerate(10)
    print ford.currentSpeed
