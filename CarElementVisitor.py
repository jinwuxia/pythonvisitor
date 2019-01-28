from abc import ABCMeta, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

class CarElementVisitor:
    __metaclass__ = ABCMeta
    @abstractmethod
    def visitBody(self, element):
        raise NotImplementedError(NOT_IMPLEMENTED)
    @abstractmethod
    def visitEngine(self, element):
        raise NotImplementedError(NOT_IMPLEMENTED)
    @abstractmethod
    def visitWheel(self, element):
        raise NotImplementedError(NOT_IMPLEMENTED)
    @abstractmethod
    def visitCar(self, element):
        raise NotImplementedError(NOT_IMPLEMENTED)
