# -*- coding: utf-8 -*-


class Node:
    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # add node in tail of list
    def add_in_tail(self, n):
        if self.head is None:
            self.head = n
        else:
            self.tail.next = n
        self.tail = n

    # printing all nodes values to console
    def print_all_nodes(self):
        node = self.head
        while node is not None:
            print(node.value)
            node = node.next

    # returning node with value="value"
    def find(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                return node
            node = node.next

        return None

    # converts LinkedList to Python list with nodes values as elements
    def to_values_list(self):
        result = []
        node = self.head

        while node is not None:
            result.append(node.value)
            node = node.next

        return result

    # return node from position 'pos'
    def get_at(self, pos):
        if (pos < 0) or (pos >= self.len()):
            return None

        i = 0
        node = self.head
        while node is not None:
            if pos == i:
                return node
            i += 1
            node = node.next

        return None

    # Deletes element from list
    # flag "all" enables deleting all value entries
    def delete(self, value, all=False):
        node = self.head
        prev = None

        while node is not None:
            # when we found node
            if node.value == value:
                # if that node is a last, update tail pointer
                if node.next is None:
                    self.tail = prev

                # if that node is a first, update head pointer and return
                if prev is None:
                    self.head = node.next
                else:
                    # set previous node pointer on the next node
                    prev.next = node.next

                # if remove only first entry, return
                if not all:
                    return
            else:
                prev = node

            node = node.next

    # cleaning list
    def clean(self):
        # Nullify head and tail pointers will be enough
        # Garbage collector will do the rest
        self.head = None
        self.tail = None

    # return list of nodes with value="value"
    def find_all(self, value):
        result = []

        node = self.head
        while node is not None:
            if node.value == value:
                result.append(node)
            node = node.next

        return result

    # return length of list
    def len(self):
        counter = 0
        node = self.head

        while node is not None:
            counter += 1
            node = node.next

        return counter

    # inserting "new_node" after "target_node"
    def insert(self, afterNode, newNode):
        # Appending element in tail if there are empty list and target node is None
        if self.len() == 0 and afterNode is None:
            self.add_in_tail(newNode)
            return

        node = self.head
        while node is not None:
            if node == newNode:
                newNode.next = node.next
                node.next = newNode

                return

            node = node.next

    # summarize l1 and l2
    # l1 and l2 - LinkedLists
    @staticmethod
    def sum_lists(l1, l2):
        if l1.len() != l2.len():
            return None

        result = LinkedList()

        l1_node = l1.head
        l2_node = l2.head

        while l1_node is not None:
            result.add_in_tail(Node(l1_node.value + l2_node.value))
            l1_node = l1_node.next
            l2_node = l2_node.next

        return result
