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

visitor1 = CarElementPrintVisitor()
visitor2 = CarElementDoVisitor()
body.accept(visitor1)
engine.accept(visitor1)
wheel.accept(visitor1)
car.accept(visitor1)

body.accept(visitor2)
engine.accept(visitor2)
wheel.accept(visitor2)
car.accept(visitor2)
