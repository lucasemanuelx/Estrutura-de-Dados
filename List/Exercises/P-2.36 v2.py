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
from enum import IntEnum, unique
from abc import ABC, abstractmethod


@unique
class Direction(IntEnum):
    LEFT = -1
    RIGHT = 1


@unique
class Strength(IntEnum):
    STRONG = 6
    WEAK = 4


class Animal(ABC):

    @abstractmethod
    def set_index(self, new_index):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def can_eat(self, next_animal):
        pass

    @abstractmethod
    def can_be_eaten(self, next_animal):
        pass

    @abstractmethod
    def can_have_baby(self, next_animal):
        pass

    @abstractmethod
    def can_fight(self, next_animal):
        pass


class Bear(Animal):

    def __init__(self, index):
        self.index = index
        self._strength = random.randrange(Strength.WEAK, Strength.STRONG, 1)

    def set_index(self, new_index):
        self.index = new_index

    def move(self):
        where = random.randrange(Direction.LEFT, Direction.RIGHT, 1)
        return self.index + where

    def can_eat(self, next_animal):
        if not isinstance(next_animal, Bear):
            return True
        else:
            return False

    def can_be_eaten(self, next_animal):
        pass

    def can_have_baby(self, next_animal):
        if isinstance(next_animal, Bear):
            if self.get_strength() == next_animal.get_strength():
                return True
        else:
            return False

    def can_fight(self, next_animal):
        if isinstance(next_animal, Bear):
            if self.get_strength() != next_animal.get_strength():
                return True
        else:
            return False

    def get_strength(self):
        return self._strength

    def _set_strength(self, new_strength):
        self._strength = new_strength

    def __repr__(self):
        return "Bear(%d)" % self.index


class Fish(Animal):

    def __init__(self, index):
        self.index = index

    def set_index(self, new_index):
        self.index = new_index

    def move(self):
        where = random.randrange(Direction.LEFT, Direction.RIGHT, 1)
        return self.index + where

    def can_eat(self, next_animal):
        pass

    def can_be_eaten(self, next_animal):
        if isinstance(next_animal, Bear):
            return True
        else:
            return False

    def can_have_baby(self, next_animal):
        if isinstance(next_animal, Fish):
            return True
        else:
            return False

    def can_fight(self, next_animal):
        pass

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
        for i in range(__qnt):
            ind = random.choice(self._aux)
            self._data[ind] = animal(ind)
            self._aux.remove(ind)

    def stream(self, turns=10):
        for i in range(turns):
            animal = self.__pick_random_animal()
            next_ind = animal.move()
            self.__print_direction(animal, next_ind)
            if 0 <= next_ind < len(self._data) and next_ind != animal.index:
                next_animal = self._data[next_ind]
                if next_animal is None:
                    self.__move_animal(animal, next_ind)
                else:
                    self.__have_baby(animal, next_animal)
                    self.__eat(animal, next_animal)
                    self.__fight(animal, next_animal)
            print(River.__str__(self))

    def __pick_random_animal(self):
        animal = None
        while animal is None:
            animal = random.choice(self._data)
        return animal

    def __move_animal(self, animal, next_ind):
        self._data.remove(animal)
        self._data.insert(next_ind, animal)
        animal.set_index(next_ind)

    def __have_baby(self, animal, next_animal):
        if animal.can_have_baby(next_animal):
            if self._data.count(None) > 0:
                baby = self._data.index(None)
                self._data.pop(baby)
                if isinstance(animal, Fish):
                    self._data.insert(baby, Fish(baby))
                    print("A new baby fish is born!", Fish(baby))
                elif isinstance(animal, Bear):
                    self._data.insert(baby, Bear(baby))
                    print("A new baby bear is born!", Bear(baby))
            else:
                print(animal, "tried to have a baby, but the river is full!")

    def __eat(self, animal, next_animal):
        if animal.can_eat(next_animal):
            print(next_animal, "has been eaten...")
            self._data[next_animal.index] = None
        elif animal.can_be_eaten(next_animal):
            print(animal, "has been eaten...")
            self._data[animal.index] = None

    def __fight(self, animal, next_animal):
        if animal.can_fight(next_animal):
            if animal.get_strength() > next_animal.get_strength():
                animal._set_strength(animal.get_strength() + 1)
                next_animal._set_strength(next_animal.get_strength() - 1)
                print(next_animal, "lost a fight")
                if(next_animal.get_strength() <= 0):
                    self._data[next_animal.index] = None
                    print(next_animal, "died in the fight")
            elif animal.get_strength() < next_animal.get_strength():
                animal._set_strength(animal.get_strength() - 1)
                next_animal._set_strength(next_animal.get_strength() + 1)
                print(animal, "lost a fight")
                if(animal.get_strength() <= 0):
                    self._data[animal.index] = None
                    print(animal, "died in the fight")


    def __print_direction(self, animal, next_ind):
        where = next_ind - animal.index
        if 0 <= next_ind < len(self._data):
            if where == Direction.LEFT:
                print(animal, "goes left")
            elif where == Direction.RIGHT:
                print(animal, "goes right")
            else:
                print(animal, "stays put")
        else:
            print(animal, "tried to leave the river, but stays put")

    def __str__(self):
        return self._data.__str__() + "\n" + "----------"


if __name__ == "__main__":
    r = River()
    print(r)
    r.stream()
