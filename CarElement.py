
class CarElement:

    def getname(self):
        print("element")

    def accept(self, visitor):
        visitor.visit(self)
