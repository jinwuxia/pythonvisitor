from CarElement import CarElement

class Wheel(CarElement):
    def __init__(self, name):
        self.name = name
    def accept(self, visitor):
        visitor.visit(self)
    def operate(self):
        print("operate wheel: " + self.name)
    def print(self):
        print("print wheel: " + self.name)
