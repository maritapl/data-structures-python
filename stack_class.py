"""
Custom Stack implementation (LIFO).

Supports:
 push
 pop
 peek
 is_empty
 size
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    s.push(10)
    s.push(20)
    print("Peek:", s.peek())      # 20
    print("Pop:", s.pop())        # 20
    print("Size:", s.size())      # 1
    print("Empty:", s.is_empty()) # False
