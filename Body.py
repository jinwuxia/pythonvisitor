from CarElement import CarElement

class Body(CarElement):
    def accept(self, visitor):
        visitor.visitBody(self)
    def operateBody(self):
        print("operate body")
    def printBody(self):
        print("print body")
    def getBody(self):
        pass
