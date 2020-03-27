from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):  # need to append before we get
        # if ring buffer is empty, and current isnt set, set current to be head
        if len(self.storage) < self.capacity and self.current is None:
            self.current = self.storage.head

        # if ring buffer isnt at capacity, just append new item to storage
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        # if we are at capacity,
        if len(self.storage) == self.capacity:
            if self.current.next is None:

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
