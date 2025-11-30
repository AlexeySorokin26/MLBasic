from base import Vehicle
from exceptions import CargoOverLoad

class Plane(Vehicle):
    def __init__(self, cargo, maxCargo, weight, fuel, fuelConsumption):
        super().__init__(weight, fuel, fuelConsumption)
        self.cargo = cargo
        self.maxCargo = maxCargo
    def LoadCargo(self, newCargo):
        if(self.cargo + newCargo > 10000):
            raise CargoOverLoad
        self.cargo = self.cargo + newCargo
    def RemoveAllCargo(self):
        tmp = self.cargo 
        self.cargo = 0
        return tmp