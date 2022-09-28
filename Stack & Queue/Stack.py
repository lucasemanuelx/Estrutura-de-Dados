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



