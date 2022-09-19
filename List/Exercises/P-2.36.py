"""
P-2.36
Write a Python program to simulate an ecosystem containing two types
of creatures, bears and fish. The ecosystem consists of a river, which is
modeled as a relatively large list. Each element of the list should be a
Bear object, a Fish object, or None. In each time step, based on a random
process, each animal either attempts to move into an adjacent list location
or stay where it is. If two animals of the same type are about to collide in
the same cell, then they stay where they are, but they create a new instance
of that type of animal, which is placed in a random empty (i.e., previously
None) location in the list. If a bear and a fish collide, however, then the
fish dies (i.e., it disappears).
"""
import random
from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def set_index(self, new_index):
        pass

    @abstractmethod
    def move(self, next_spot):
        pass

    @abstractmethod
    def eat(self, next_animal):
        pass

    @abstractmethod
    def have_baby(self, next_animal):
        pass


class Bear(Animal):

    def __init__(self, index):
        self.index = index

    def set_index(self, new_index):
        self.index = new_index

    def move(self, next_spot):
        if next_spot:
            return False
        else:
            return True

    def eat(self, next_animal):
        if not isinstance(next_animal, Bear):
            return True
        else:
            return False

    def have_baby(self, next_animal):
        if isinstance(next_animal, Bear):
            return True
        else:
            return False

    def __repr__(self):
        return "Bear(%d)" % self.index


class Fish(Animal):

    def __init__(self, index):
        self.index = index

    def set_index(self, new_index):
        self.index = new_index

    def move(self, next_spot):
        if next_spot:
            return False
        else:
            return True

    def eat(self, next_animal):
        pass

    def have_baby(self, next_animal):
        if isinstance(next_animal, Fish):
            return True
        else:
            return False

    def __repr__(self):
        return "Fish(%d)" % self.index


class River:
    def __init__(self, length=15):
        self._data = [None] * length
        self._aux = []
        self.__populate()

    def __populate(self):
        self._aux = list(range(len(self._data)))
        random.shuffle(self._aux)
        self.__generate_animal(Bear)
        self.__generate_animal(Fish)

    def __generate_animal(self, animal):
        __qnt = round(len(self._data) * 0.35)
        print(__qnt)
        for i in range(__qnt):
            ind = random.choice(self._aux)
            self._data[ind] = animal(ind)
            self._aux.remove(ind)

    def __str__(self):
        return self._data.__str__() + "\n" + "----------"


if __name__ == "__main__":
    r = River()
    print(r)
