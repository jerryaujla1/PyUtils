#!/usr/bin/env python

class Loops(object):

    def __init__(self):
        pass

    def loop_size(self, node): # Use instance of a linked list
        slow = node
        fast = node
        while fast is not None:
            slow =slow.next
            if fast.next is not None:
                fast = fast.next.next
            else:
                return False
            if slow == fast:
                count = 0
                while slow is not None:
                    slow = slow.next
                    count+=1
                    if slow == fast:
                        return count
                return True
        return False

Loops = Loops()

class Node(object):

    def __init__(self, val): # Initialize with root node as val
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = Node(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = Node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def lookup(self, val, parent=None):
        if val < self.val:
            if self.left is None:
                return None, None
            return self.left.lookup(val, self)
        elif val > self.val:
            if self.right is None:
                return None, None
            return self.right.lookup(val, self)
        else:
            return self, parent

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print self.val
        if self.right:
            self.right.print_tree()
