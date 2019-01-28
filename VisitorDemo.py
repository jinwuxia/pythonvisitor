from Car import Car
from CarElementDoVisitor import CarElementDoVisitor
from CarElementPrintVisitor import CarElementPrintVisitor

car = Car()
car.accept(CarElementPrintVisitor())
car.accept(CarElementDoVisitor())
