class Stack:
    def __init__(self, stack=[]):
        self.stack = stack

    # check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # added alelemnt to the stack
    def push(self, element):
        return self.stack.append(element)

    # remove first element from the stack
    def pop(self):
        if self.is_empty():
            return f"Stack is empty"

        return self.stack.pop()

    # first element on the stack
    def peek(self):
        if self.is_empty():
            return f"Stack is empty"

        return self.stack[len(self.stack)-1]

    def __str__(self) -> str:
        return f"{self.stack}"


class Queue:
    def __init__(self) -> None:
        self.queue = []

    # add element to the queue
    def enqueue(self, element):
        self.queue.append(element)
    
    #remove element from the queue
    def dequeue(self):
        if self.size == 0:
            return "Queue is empty"
        return self.queue.pop(0)
    
    # return size of queue
    @property
    def size(self):
        return len(self.queue)

    def __str__(self) -> str:
        return f'{self.queue}'


class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.circular_queue = [None] * size
        self.head = -1
        self.tail = -1

    # add to the queue
    def enqueue(self, element):
        if (self.tail + 1) % self.size == self.head:
            return f'The circular queue is full'
        elif self.head == -1:
            self.head = 0
            self.tail = 0
            self.circular_queue[self.tail] = element
        else:
            self.tail = (self.tail + 1) % self.size
            self.circular_queue[self.tail] = element

    # remove element front element from the queue
    def dequeue(self):
        if self.head == -1:
            return f'The circular queue is empty'
        elif self.head == self.tail:
            temp = self.circular_queue[self.head]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.circular_queue[self.head]
            self.head = (self.head + 1) % self.size
            return temp
    
    def __str__(self) -> str:
        if self.head == -1:
            return f'Circular queue is empty'
        elif self.tail > self.head:
            return f'{[self.circular_queue[i] for i in range(self.head, self.tail + 1)]}'
        else:
            cq_1 = [self.circular_queue[i] for i in range(self.head, self.size)]
            cq_2 = [self.circular_queue[i] for i in range(0, self.tail + 1)]

            return f'{[i for i in cq_2 + cq_1]}'

