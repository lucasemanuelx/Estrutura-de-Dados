from abc import ABC, abstractmethod


class ListADT(ABC):

    @abstractmethod
    def insert(self, index, elem):
        """Inserts <elem> in <index>"""
        pass

    @abstractmethod
    def remove(self, elem):
        """Removes first occurence of <elem>"""
        pass

    @abstractmethod
    def remove_all(self, elem):
        """Removes all occurences of <elem>"""
        pass

    @abstractmethod
    def remove_at(self, index):
        """Removes node at <index>"""
        pass

    @abstractmethod
    def count(self, elem):
        """Counts <elem> in list"""
        pass

    @abstractmethod
    def clear(self):
        """Clears lists"""
        pass

    @abstractmethod
    def index(self, elem):
        """Returns index of <elem>"""
        pass

    @abstractmethod
    def append(self, elem):
        """Appends <elem> at the end of the list """
        pass

    @abstractmethod
    def replace(self, index, elem):
        """Replaces node at <index> with <elem>"""
        pass

    @abstractmethod
    def length(self):
        """Returns length of the list"""
        pass


class DoublyLinkedList(ListADT):

    class _Node:
        def __init__(self, elem=None, next=None, prev=None):
            self._elem = elem
            self._next = next
            self._prev = prev

        def __str__(self):
            if self._next is None:
                return self._elem.__str__()
            else:
                return self._elem.__str__() + "<->"

    def __init__(self):
        self._header = self._Node()
        self._trailer = self._Node()
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self.length = 0

    def insert(self, index, elem):
        pass

    def remove(self, elem):
        pass

    def remove_all(self, elem):
        pass

    def remove_at(self, index):
        pass

    def count(self, elem):
        pass

    def clear(self):
        pass

    def index(self, elem):
        pass

    def append(self, elem):
        pass

    def replace(self, index, elem):
        pass

    def length(self):
        pass
