from CarElementVisitor import CarElementVisitor


class CarElementDoVisitor(CarElementVisitor):
    def visitBody(self, body):
        body.operateBody()

    def visitCar(self, car):
        car.operateCar()

    def visitWheel(self, wheel):
        wheel.operateWheel()

    def visitEngine(self, engine):
        engine.operateEngine()
