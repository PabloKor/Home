"""
создайте класс `Car`, наследник `Vehicle`
"""

from homewor_02.base import Vehicle


class Car(Vehicle):
    engine = 0

    def set_engine(self, class_engine):
        self.engine = class_engine
