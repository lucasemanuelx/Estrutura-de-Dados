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
