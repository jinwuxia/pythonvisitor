from CarElementVisitor import CarElementVisitor

class CarElementDoVisitor(CarElementVisitor):
    def visitBody(self, body):
        print("Moving my body.")

    def visitCar(self, car):
        print("Starting my car.")

    def visitWheel(self, wheel):
        print("Kicking my {} wheel.".format(wheel.name))

    def visitEngine(self, engine):
        print("Starting my engine.")
