from abc import ABCMeta, abstractmethod
NOT_IMPLEMENTED = "You should implement this."

class CarElementVisitor:
    __metaclass__ = ABCMeta
     
    @abstractmethod
    def visitBody(self, element):
        element.getBody()

    @abstractmethod
    def visitEngine(self, element):
        element.getEngine()

    @abstractmethod
    def visitWheel(self, element):
        element.getWheel()

    @abstractmethod
    def visitCar(self, element):
        element.getCar()
	
    def tranverse(self):
        pass
           
