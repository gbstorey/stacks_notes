class Stack:
    def __init__(self, max_size):
        self.maxSize = max_size
        self.list = []

    def __str__(self):
        values = reversed(self.list)
        values = [str(x) for x in values]
        return '\n'.join(values)

    def is_empty(self):
        # O(1) time and space complexity
        if not self.list:
            return True
        else:
            return False

    def is_full(self):
        # O(1) time and space complexity
        if len(self.list) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        # O(1) time and space complexity
        if self.is_full():
            return "The stack is full"
        else:
            self.list.append(value)
            return "The element has been successfully inserted"

    def pop(self):
        # O(1) time and space complexity
        if self.is_empty():
            return "The stack is empty"
        else:
            return self.list.pop()

    def peek(self):
        # O(1) time and space complexity
        if self.is_empty():
            return "There are no elements in the stack."
        else:
            return self.list[-1]

    def delete(self):
        # O(1) time and space complexity
        self.list = None


customStack = Stack(4)
print(customStack.is_empty())
print(customStack.is_full())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
