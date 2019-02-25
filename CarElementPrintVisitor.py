from CarElementVisitor import CarElementVisitor

class CarElementPrintVisitor(CarElementVisitor):
    def visit(self, element):
        element.print()
