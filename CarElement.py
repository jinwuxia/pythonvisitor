from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

class CarElement:
    __metaclass__ = ABCMeta

    def getname(self):
        print("element")

    @abstractmethod
    def accept(self, visitor):
        visitor.visit(self)
