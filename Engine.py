from CarElement import CarElement

class Engine(CarElement):
    def accept(self, visitor):
        visitor.visitEngine(self)
    def operateEngine(self):
        print("operate engine")
    def printEngine(self):
        print("print engine")
