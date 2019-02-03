from CarElement import CarElement

class Wheel(CarElement):
    def __init__(self, name):
        self.name = name
    def accept(self, visitor):
        visitor.visitWheel(self)
    def operateWheel(self):
        print("operate wheel: " + self.name)
    def printWheel(self):
        print("print wheel: " + self.name)
