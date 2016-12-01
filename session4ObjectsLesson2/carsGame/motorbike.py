from vehicle import Vehicle

class Motorbike(Vehicle):
    def __init__(self, make):
        Vehicle.__init__(self, make, 100)

    def printMe(self):
        print "vroooom"

if __name__ == '__main__':
    suzuki = Motorbike('suzuki')
    suzuki.changeGear(2)
    suzuki.printMe()
