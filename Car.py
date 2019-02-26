from CarElement import CarElement
from Wheel import Wheel
from Body import Body
from Engine import Engine

class Car(CarElement):
    def __init__(self):
        self.elements = [
            Wheel("front left"), Wheel("front right"),
            Wheel("back left"), Wheel("back right"),
            Body(), Engine()
        ]

    def accept(self, visitor):
        visitor.visitCar(self)
    def operateCar(self):
        print("operate car")
    def printCar(self):
        print("print car")
    def getCar(self):
        pass
