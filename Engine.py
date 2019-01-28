from CarElement import CarElement

class Engine(CarElement):
    def accept(self, visitor):
        visitor.visitEngine(self)
