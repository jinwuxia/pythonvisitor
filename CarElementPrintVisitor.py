from CarElementVisitor import CarElementVisitor

class CarElementPrintVisitor(CarElementVisitor):
    def visitBody(self, body):
        print("Visiting body.")

    def visitCar(self, car):
        print("Visiting car.")

    def visitWheel(self, wheel):
        print("Visiting {} wheel.".format(wheel.name))

    def visitEngine(self, engine):
        print("Visiting engine.")
