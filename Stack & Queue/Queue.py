from abc import ABC, abstractmethod


class QueueADT(ABC):

    @abstractmethod
    def enqueue(self, elem):
        """Enqueues <eleme>"""
        pass

    @abstractmethod
    def dequeue(self):
        """Dequeues element from queue"""
        pass

    @abstractmethod
    def first(self):
        """Returns a reference to the first element of the queue, without removing it"""
        pass

    @abstractmethod
    def is_empty(self):
        """Returns True if the queue does not contain any elements"""
        pass


class Queue(QueueADT):
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
        self._tail = None
        self._length = 0