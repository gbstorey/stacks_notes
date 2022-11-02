class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        cur_node = self.head
        while cur_node:
            yield cur_node
            cur_node = cur_node.next


class Stack:
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    # All operations are O(1) in time and space complexity

    def is_empty(self):
        if self.LinkedList.head is None:
            return True
        else:
            return False

    def push(self, value):
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        if self.is_empty():
            return "The stack is empty."
        else:
            node_value = self.LinkedList.head.value
            self.LinkedList.head = self.LinkedList.head.next
            return node_value

    def peek(self):
        if self.is_empty():
            return "The stack is empty."
        else:
            return self.LinkedList.head.value

    def delete(self):
        self.LinkedList.head = None


customStack = Stack()
customStack.push(1)
print(customStack.pop())
print(customStack)
