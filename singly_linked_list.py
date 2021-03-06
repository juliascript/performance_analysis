#!python

from __future__ import print_function
import time
start_time = time.time()


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data

       th(1) running time to create two properties"""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node

        th(n) running time to loop over entire list to print"""
        return 'Node({})'.format(repr(self.data))


class LinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list; append the given items, if any

        Best case running time: om(n-m) if no iterable is passed in
       Worst case running time: O(n) for length of iterable"""
        self.head = None
        self.tail = None
        if iterable:
            for item in iterable:
                self.append(item)

    def __repr__(self):
        """Return a string representation of this linked list

        th(n) running time to loop over entire list to print"""
        return 'LinkedList({})'.format(self.as_list())

    def as_list(self):
        """Return a list of all items in this linked list

        th(n) running time to loop over entire list to print"""
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            # result.append(current)
            current = current.next
        return result

    def is_empty(self):
        """Return True if this linked list is empty, or False

        th(1) running time to check value of property"""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes

        th(n) running time to loop over entire list to print"""
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def append(self, item):
        """Insert the given item at the tail of this linked list

        th(1) running time to (re)assign tail"""
        node = Node(item)
        if self.tail is not None:
            currentTailNode = self.tail
            currentTailNode.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def prepend(self, item):
        """Insert the given item at the head of this linked list

        th(1) to access head and replace"""
        # TODO: prepend given item
        node = Node(item)
        if self.head is not None:
            currentHeadNode = self.head
            node.next = currentHeadNode
            self.head = node
        else: 
            self.head = node
            self.tail = node

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError

        Best case running time: om(1) if item is near the head of the list.
       Worst case running time: O(n) if item is near the tail of the list or
       not present and we need to loop through all n nodes in the list."""
        current = self.head
        try:
            if current.data == item:
                if current.data == self.tail.data:
                    self.head = None
                    self.tail = None
                    return
                else: 
                    self.head = current.next
                return None

            while current.next is not None: 
                if current.next.data == item:
                    #remove item
                    if current.next == self.tail:
                        self.tail = current
                        current.next = None
                    else:
                        current.next = current.next.next

                    return 
                else: 
                    current = current.next
        except AttributeError:
            raise ValueError

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality

        Best case running time: om(1) if item is near the head of the list.
       Worst case running time: O(n) if item is near the tail of the list or
       not present and we need to loop through all n nodes in the list."""
        # TODO: find item where quality(item) is True
        current = self.head

        try: 
            while current.data is not None:
                if quality(current.data) is True: 
                    # return current.data
                    return time.time() - start_time
                else:
                    current = current.next
            # return None
            return time.time() - start_time
        except AttributeError:
            return time.time() - start_time

    def __iter__(self):
        """Make linked list iterable

        th(1) to yield current"""
        current = self.head
        while current is not None:
            yield current
            current = current.next