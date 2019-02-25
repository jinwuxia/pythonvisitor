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
        visitor.visit(self)
    def operate(self):
        print("operate car")
    def print(self):
        print("print car")
