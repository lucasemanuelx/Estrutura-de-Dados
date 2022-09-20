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
            if self._next._next is None:
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
        if self._length == 0:
            self.__insert_in_empty_list(new_node)
        else:
            self.__insert_middle(new_node, index)

    def __insert_in_empty_list(self, new_node):
        self._header._next = new_node
        self._trailer._prev = new_node
        new_node._next = self._trailer
        new_node._prev = self._header
        self._length += 1

    def __insert_middle(self, new_node, index):
        aux = self._header
        for i in range(index + 1):
            aux = aux._next
        aux._prev._next = new_node
        aux._prev = new_node
        new_node._next = aux
        new_node._prev = aux._prev
        self._length += 1

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

    def __str__(self):
        if self._header:
            result = ''
            aux = self._header._next
            result += aux.__str__()
            while aux._next is not self._trailer:
                aux = aux._next
                result += aux.__str__()
            return result
        else:
            return '||'


if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert(0, 5)
    dll.insert(0, 9)
    dll.insert(1, 3)
    dll.insert(2, 4)
    dll.insert(50, 8)
    dll.insert(65, 2)
    dll.remove(9)
    print(dll)
