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
            if self._next._elem is None:
                return self._elem.__str__()
            else:
                return self._elem.__str__() + "<->"

    def __init__(self):
        self._header = self._Node()
        self._trailer = self._Node()
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._length = 0

    def insert(self, index, elem):
        new_node = self._Node(elem)
        if index > self._length:
            index = self._length
        self.__insert_middle(new_node, index)

    def __insert_middle(self, new_node, index):
        aux = self._header
        for i in range(index):
            aux = aux._next
        new_node._next = aux._next
        new_node._prev = aux
        aux._next._prev = new_node
        aux._next = new_node
        self._length += 1

    def remove(self, elem):
        if self._header._next == self._trailer:
            pass
        aux = self._header
        found_elem = False
        while aux._next is not None and not found_elem:
            if aux._elem == elem:
                aux._prev._next = aux._next
                aux._next._next = aux._prev
                aux = aux._next
                self._length -= 1
                found_elem = True
            else:
                aux = aux._next

    def remove_all(self, elem):
        if self._header._next == self._trailer:
            pass
        else:
            aux = self._header
            while aux._next is not None:
                if aux._elem == elem:
                    aux._prev._next = aux._next
                    aux._next._next = aux._prev
                    aux = aux._next
                    self._length -= 1
                else:
                    aux = aux._next

    def remove_at(self, index):
        if index >= self._length:
            index = self._length - 1
        if self._header._next == self._trailer:
            pass
        else:
            aux = self._header
            for i in range(index + 1):
                aux = aux._next
            aux._prev._next = aux._next
            aux._next._next = aux._prev
            self._length -= 1

    def count(self, elem):
        count = 0
        aux = self._header._next
        while aux._elem:
            if aux._elem == elem:
                count += 1
            aux = aux._next
        return count

    def clear(self):
        self._header = self._Node()
        self._trailer = self._Node()
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._length = 0

    def index(self, elem):
        if self._header._next is self._trailer:
            raise Exception("The list is empty!")
        aux = self._header._next
        count = 0
        while aux._elem != elem:
            aux = aux._next
            count += 1
        return count

    def append(self, elem):
        pass

    def replace(self, index, elem):
        pass

    def length(self):
        return self._length

    def __str__(self):
        if self._header._next is not self._trailer:
            result = ''
            aux = self._header._next
            result += aux.__str__()
            while aux._next is not self._trailer:
                aux = aux._next
                result += aux.__str__()
            return result
        else:
            return '||'

