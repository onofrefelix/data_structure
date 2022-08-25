from typing import TypeVar

T = TypeVar('T')


class Node(object):
    def __init__(self, value: T) -> None:
        self.data = value
        self.next = None

    def get_value(self):
        return self.data

    def get_next(self):
        return self.next

    def set_value(self, val: T):
        self.data = val

    def set_next(self, other):
        self.next = other


class LinkedList(object):
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add_item(self, item):
        current = Node(item)
        current.set_next(self.head)
        self.head = current

    def size(self) -> int:
        current = self.head
        count = 0
        while current is not None:
            count +=1
            current = current.get_next()

        return count

    def is_value_exist(self, value):
        current = self.head
        is_exists = False
        while current is not None:
            if current.get_value() == value:
                is_exists = True
            current = current.get_next()
        return is_exists

    def remove_item(self, value: T) -> bool:
        current = self.head
        previous: Node = None
        found = False

        while current is not None:
            if current.get_value() == value:
                found = True
                break
            else:
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())

        return found



