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
    def length(self):
        """Returns length of the list"""
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
    def append(self, elem):
        """Appends <elem> at the end of the list """
        pass

    @abstractmethod
    def replace(self, index, elem):
        """Replaces node at <index> with <elem>"""
        pass


class LinkedList(ListADT):
    class Node:

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
        self._tail = self._head
        self._length = 0

    def insert(self, index, elem):
        new_node = self.Node(elem)
        if self._head is None:  # insert in empty list
            self._head = new_node
            self._tail = new_node
        else:
            if index == 0:
                self.__insert_start(new_node)
            elif 0 < index < self._length:
                self.__insert_middle(index, new_node)
            elif index >= self._length:
                self.__insert_end(new_node)
        self._length += 1

    def __insert_start(self, new_node):
        new_node._next = self._head
        self._head = new_node

    def __insert_middle(self, index, new_node):
        prev = self._head
        aux = prev._next
        for i in range(index - 1):
            prev = aux
            aux = aux._next
        prev._next = new_node
        new_node._next = aux

    def __insert_end(self, new_node):
        aux = self._head
        while aux._next:
            aux = aux._next
        aux._next = new_node

    def remove(self, elem):
        if self._head is None:  # removing in empty list
            pass
        else:
            found_element = False
            prev = self._head
            aux = prev._next
            if self._head._elem == elem:  # removing from head
                self._head = aux
                found_element = True
                self._length -= 1
            while prev._next and not found_element:
                if aux._elem == elem:
                    prev._next = aux._next
                    aux = aux._next
                    found_element = True
                    self._length -= 1
                else:
                    prev = aux
                    aux = aux._next

    def count(self, elem):
        count = 0
        aux = self._head
        while aux:
            if aux._elem == elem:
                count += 1
            aux = aux._next
        return count

    def clear(self):
        self._head = None
        self._tail = self._head
        self._length = 0

    def index(self, elem):
        aux = self._head
        found_element = False
        index = -1
        while aux and not found_element:
            if aux._elem == elem:
                found_element = True
            index += 1
            aux = aux._next
        return index

    def length(self):
        return self._length

    def remove_all(self, elem):
        pass

    def remove_at(self, index):
        pass

    def append(self, elem):
        pass

    def replace(self, index, elem):
        pass

    def __str__(self):
        if self._head is not None:
            result = ''
            aux = self._head
            result += aux.__str__()
            while aux._next:
                aux = aux._next
                result += aux.__str__()
            return result
        else:
            return '||'


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert(8, 0)
    print(ll)
    ll.insert(0, 5)
    print(ll)
    ll.insert(1, 8)
    print(ll)
    ll.insert(3, 2)
    ll.insert(0, 3)
    ll.insert(1, 0)
    ll.insert(50, 0)
    print(ll)
    print(ll.length())
    # ll.remove(0)
    ll.remove(1)
    ll.remove(3)
    ll.remove(4)
    # ll.remove(1)
    ll.remove(5)
    ll.remove(0)
    print(ll.length())
    print(ll)
