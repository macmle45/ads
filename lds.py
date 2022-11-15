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


class PriorityQueue:
    def __init__(self):
        self.array = []
    
    @property
    def __size(self):
        return len(self.array)

    def __heapify(self, i):
        # largest index
        largest = i

        # left child index
        left = 2 * i + 1

        # right child index
        right = 2 * i + 2

        if left < self.__size and self.array[left] > self.array[i]:
            largest = left

        if right < self.__size and self.array[right] > self.array[largest]:
            largest = right

        # swap
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.__heapify(largest)

    # insert new element to the queue
    def insert(self, new_node: int):
        if self.__size == 0:
            self.array.append(new_node)
        else:
            self.array.append(new_node)

            # heapify (from the last element)
            for i in range((self.__size // 2) - 1, -1, -1):
                self.__heapify(i)

    # delete element from the priority queue
    def removeNode(self, ntbd):
        # init index
        i = 0

        # find index of node to be deleted
        for i in range(0, self.__size):
            if ntbd == self.array[i]:
                break
        
        # swap ntbd with last element
        self.array[i], self.array[self.__size - 1] = self.array[self.__size - 1], self.array[i]

        # delete last element
        self.array.remove(self.array[self.__size - 1])

        # heapify tree
        for i in range((self.__size // 2) - 1, -1, -1):
            self.__heapify(i)
        


    @property
    def peek(self):
        pass

    def extract(self, type):
        pass

    def __str__(self) -> str:
        return f'{self.array}'
