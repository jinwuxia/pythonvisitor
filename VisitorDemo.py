from Car import Car
from Body import Body
from Engine import Engine
from Wheel import Wheel

from CarElementDoVisitor import CarElementDoVisitor
from CarElementPrintVisitor import CarElementPrintVisitor

body = Body()
engine = Engine()
wheel = Wheel("front")
car = Car()

body.accept(CarElementPrintVisitor())
engine.accept(CarElementPrintVisitor())
wheel.accept(CarElementPrintVisitor())
car.accept(CarElementPrintVisitor())

body.accept(CarElementDoVisitor())
engine.accept(CarElementDoVisitor())
wheel.accept(CarElementDoVisitor())
car.accept(CarElementDoVisitor())
