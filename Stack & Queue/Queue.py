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

    def enqueue(self, elem):
        new_node = self._Node(elem)
        if self._length == 0:
            self._head = new_node
        else:
            self._tail._next = new_node
        self._tail = new_node
        self._length += 1

    def dequeue(self):
        if not self._head:
            raise Exception("The queue is empty")
        popped = self._head
        self._head = self._head._next
        self._length -= 1
        return popped

    def first(self):
        if not self._head:
            raise Exception("The queue is empty")
        return self._head._elem

    def is_empty(self):
        return self._length == 0

    def __str__(self):
        if self._head:
            result = ''
            aux = self._head
            result += aux.__str__()
            while aux._next:
                aux = aux._next
                result += aux.__str__()
            return result
        else:
            return '||'
