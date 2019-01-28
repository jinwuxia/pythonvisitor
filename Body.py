from CarElement import CarElement

class Body(CarElement):
    def accept(self, visitor):
        visitor.visitBody(self)
