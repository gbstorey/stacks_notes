# No size limit with Python lists, but speed problems due to memory allocation

class Stack:
    def __init__(self):
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

    def push(self, value):
        # Amortized O(1) -> O(n^2) time complexity depending on memory.
        # O(1) space complexity.
        self.list.append(value)
        return "The element has been successfully inserted"

    def pop(self):
        # O(1) time and space complexity
        if self.is_empty():
            return "There are no elements in the stack."
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


customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
