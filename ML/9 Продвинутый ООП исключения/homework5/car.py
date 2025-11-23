from base import Vehicle
from engine import Engine

class Car(Vehicle):
    def __init__(self, engine, weight, fuel, fuelConsumption):
        super().__init__(weight, fuel, fuelConsumption)
        self.engine = engine
    def SetEngine(self, engine):
        self.engine = engine
