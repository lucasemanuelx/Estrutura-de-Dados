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
        if self._head is None:  # removing from empty list
            pass
        else:
            found_element = False
            prev = self._head
            aux = prev._next
            if self._head._elem == elem:  # removing from head
                self.__remove_head()
                found_element = True
            while prev._next and not found_element:
                if aux._elem == elem:
                    prev._next = aux._next
                    aux = aux._next
                    found_element = True
                    self._length -= 1
                else:
                    prev = aux
                    aux = aux._next

    def remove_all(self, elem):
        if self._head is None:  # removing from empty list
            pass
        else:
            while self._head._elem == elem:
                self.__remove_head()
            prev = self._head
            aux = prev._next
            while aux:
                if aux._elem == elem:
                    prev._next = aux._next
                    aux = aux._next
                    self._length -= 1
                else:
                    prev = aux
                    aux = aux._next

    def remove_at(self, index):
        if self._head is None:
            pass
        else:
            prev = self._head
            aux = prev._next
            if index == 0:
                self.__remove_head()
            else:
                for i in range(index-1):
                    prev = aux
                    aux = aux._next
                prev._next = aux._next
                self._length -= 1

    def __remove_head(self):
        self._head = self._head._next
        self._length -= 1

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

    def append(self, elem):
        aux = self._head
        while aux._next:
            aux = aux._next
        aux._next = self.Node(elem)
        self._length += 1

    def replace(self, index, elem):
        

    def length(self):
        return self._length

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
    ll.insert(0, 7)
    ll.insert(0, 6)
    ll.insert(0, 5)
    ll.insert(0, 4)
    ll.insert(0, 3)
    ll.insert(0, 2)
    ll.append(500)
    ll.insert(0, 1)
    print(ll)
    print(ll.length())
    # ll.remove_all(3)
    ll.remove_at(0)
    ll.append(89)
    print(ll.length())
    print("lista", ll)
