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




