from CarElement import CarElement

class Engine(CarElement):
    def accept(self, visitor):
        visitor.visit(self)
    def operate(self):
        print("operate engine")
    def print(self):
        print("print engine")
