from homework_02.exceptions import LowFuelError, NotEnoughFuel
from abc import ABC

class Vehicle(ABC):
    def __init__(self,
                 weight=300,
                 fuel=10,
                 fuel_consumption=1,
                 ):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = False

    def start(self):
        if self.started:
            print("Let's go!")
        else:
            if self.fuel > 0:
                self.started = True
                print('Transport ready to go!')
            else:
                raise LowFuelError('In the tank there is no fuel.')

    def move(self, distance):
        amount_of_fuel = self.fuel_consumption * distance
        if amount_of_fuel <= self.fuel:
            self.fuel -= amount_of_fuel
            return f'in the tank left {self.fuel}'
        else:
            raise NotEnoughFuel()


