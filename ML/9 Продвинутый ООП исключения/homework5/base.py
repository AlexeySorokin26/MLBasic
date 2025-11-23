from exceptions import LowFuelError, NotEnoughFuel
from abc import ABC

class Vehicle(ABC):
    def __init__(self, weight, fuel, fuelConsumption):
        self.started = False
        self.weight = weight
        self.fuel = fuel
        self.fuelConsumption = fuelConsumption
    def start(self):
        if(not self.started):
            if(self.fuel > 0):
                self.started = True
            else
                raise LowFuelError("Not enough fuel")
    def move(self, distance):
        fuelToConsume = distance / 10 # 10 liter per 1 km
        if(fuelToConsume > self.fuel):
            raise NotEnoughFuel("Not enough fuel")
        self.fuel = self.fuel - fuelToConsume