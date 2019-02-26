
from CarElementVisitor import CarElementVisitor

class CarElementPrintVisitor(CarElementVisitor):
    def visitBody(self, body):
        body.printBody()

    def visitCar(self, car):
        car.printCar()

    def visitWheel(self, wheel):
        wheel.printWheel()

    def visitEngine(self, engine):
        engine.printEngine()
