from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

class CarElement:
    __metaclass__ = ABCMeta

    @abstractmethod
    def accept(self, visitor):
        visitor.tranverse()
