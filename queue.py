class Node:
    def __init__(self, value, next=None, prev=None):
        self.next = next
        self.prev = prev
        self.value = value

    def is_head(self):
        return self.next is None

    def is_tail(self):
        return self.prev is None


class Queue:
    def __init__(self):
        self._size = 0
        self._head = None
        self._tail = None

    def push_back(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = self._tail = node
        else:
            self._tail.prev = node
            node.next = self._tail
            self._tail = node

    def pop_front(self):
        if self.is_empty():
            raise Exception()
        if len(self) == 1:
            resp = self._head
            self._head = self._tail = 0
            return resp
        node = self._head
        self._head = self._head.prev
        self._head.next = 0
        return node.value

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return self._size


