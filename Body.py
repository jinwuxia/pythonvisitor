from CarElement import CarElement

class Body(CarElement):
    def accept(self, visitor):
        visitor.visit(self)
    def operate(self):
        print("operate body")
    def print(self):
        print("print body")
