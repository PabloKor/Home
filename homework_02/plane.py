"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homewor_02.base import Vehicle
from homewor_02.exceptions import CargoOverload


class Plane(Vehicle):
    def __init__(self, max_cargo, weight=300, fuel=20, fuel_consumption=2):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = 12000

    def load_cargo(self, new_cargo):
        if self.cargo + new_cargo <= self.max_cargo:
            self.cargo += new_cargo
            return f'Total weight equals {self.cargo}.'
        else:
            raise CargoOverload()

    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo


