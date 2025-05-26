from abc import ABC , abstractmethod

class vehicle(ABC):
    @abstractmethod
    def startEngine(self):
        pass
    
class car(vehicle):
    def startEngine(self):
        print("A car starts with a roar")  
        
class Motorbike(vehicle):
    def startEngine(self):
        print("A motorbike starts with a low sound") 
        
#instantiation
car1=car()
Motor=Motorbike()              

car1.startEngine()
Motor.startEngine()