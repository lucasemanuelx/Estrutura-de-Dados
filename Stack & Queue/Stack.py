from abc import ABC, abstractmethod


class StackADT(ABC):

    @abstractmethod
    def push(self, elem):
        """Adds <elem> to the top of the stack"""
        pass

    @abstractmethod
    def pop(self):
        """Removes and returns the top element from the stack"""
        pass

    @abstractmethod
    def top(self):
        """Returns a reference to the top element of the stack, without removing it"""
        pass

    @abstractmethod
    def is_empty(self):
        """Returns True if the stack does not contain any elements"""
        pass


class Stack(StackADT):
    class _Node:
        def __init__(self, elem=None, next=None):
            self._elem = elem
            self._next = next

        def __str__(self):
            if self._next is None:
                return self._elem.__str__()
            else:
                return self._elem.__str__() + "->"

    def __init__(self):
        self._head = None
        self._length = 0
