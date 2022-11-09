class Stack:
    def __init__(self, stack=[]):
        self.stack = stack

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, element):
        return self.stack.append(element)

    def pop(self):
        if self.is_empty():
            return f"Stack is empty"

        return self.stack.pop()

    def __str__(self) -> str:
        return f"{self.stack}"
