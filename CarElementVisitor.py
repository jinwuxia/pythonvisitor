from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

class CarElementVisitor:
    __metaclass__ = ABCMeta

    @abstractmethod
    def visit(self, element):
        print(element.getname())
