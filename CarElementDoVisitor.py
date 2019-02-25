from CarElementVisitor import CarElementVisitor

class CarElementDoVisitor(CarElementVisitor):
    def visit(self, element):
        element.operate()
