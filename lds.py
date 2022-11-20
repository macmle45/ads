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
        """
        Return root node
        """
        return self.array[0]

    @property
    def extract(self):
        """
        Extract-Max: return the node with maximum value after removing it from a Max Heap
        Extract-Min: return the node with minimum value after removing it from a Min Heap
        """
        rootNode = self.array[0]
        self.removeNode(rootNode)

        return rootNode

    def __str__(self) -> str:
        return f'{self.array}'


class Deque:
    def __init__(self):
        self.items = []

    @property
    def __size(self) -> int:
        return len(self.items)

    def addFront(self, el):
        return self.items.insert(0, el)

    def addRear(self, el):
        return self.items.append(el)

    def removeFront(self):
        if self.__size == 0:
            return 'Queue is empty'
        return self.items.pop(0)

    def removeRear(self):
        if self.__size == 0:
            return 'Queue is empty'
        return self.items.pop()

    def __str__(self) -> str:
        return f'{self.items}'


class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_front(self, data):       
        new_item = Node(data)
        new_item.next = self.head
        self.head = new_item

    def insert_rear(self, data):
        new_item = Node(data)

        if self.head == None:
            self.head = new_item
        else:
            element = self.head

            # traverse to the last element of linked list
            while element.next:
                element = element.next
            
            element.next = new_item

    def insert_middle(self, data, index):
        # list is empty
        if not self.head:
            self.head = Node(data)
        else:
            new_item = Node(data)

            # traverse to element at given position
            element = self.head
            counter = 1

            while counter < index:
                if element.next != None:
                    element = element.next
                
                counter += 1
                
            new_item.next = element.next
            element.next = new_item

    def delete_front(self):
        self.head = self.head.next

    def delete_rear(self):
        element = self.head

        while element.next.next != None:
            element = element.next

        element.next = None

    def delete_middle(self, index):
        element = self.head
        counter = 1

        while counter < index:
            if element.next != None:
                element = element.next

            counter += 1

        element.next = element.next.next

    def search_list(self, data):
        current = self.head

        while current != None:
            if current.item == data:
                return True
            else:
                current = current.next
        
        return False

    def sort_list(self):
        current = self.head
        index = None

        if current is None:
            return
        else:
            while current is not None:
                index = current.next

                while index is not None:
                    if current.item > index.item:

                        # swap
                        current.item, index.item = index.item, current.item
                
                    index = index.next
                current = current.next

    # traverse
    def __str__(self) -> str:
        element = self.head
        traverse_result = '[head]-->'

        while element != None:
            traverse_result += f'[{element.item}]-->'
            element = element.next

        traverse_result += '[null]'

        return traverse_result

    @property
    def length(self):
        counter = 0
        element = self.head

        while element != None:
            element = element.next
            counter += 1

        return counter

    def get_index(self, data):
        element = self.head
        counter = 0

        while element.next is not None:
            if element.item == data:
                return counter
            
            element = element.next
            counter += 1

        return False


class DoubleLinkedNode:
    def __init__(self, item):
        self.prev = None
        self.next = None
        self.item = item


class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_front(self, data):
        new_item = DoubleLinkedNode(data)

        new_item.prev = None
        new_item.next = self.head
        
        if self.head is not None:
            new_item.next.prev = new_item

        self.head = new_item


    def __str__(self) -> str:
        double_linked_list = '[head]-->'
        element = self.head

        while element is not None:
            double_linked_list += f'[{element.item}]-->'
            element = element.next

        double_linked_list += '-->[null]'

        return double_linked_list
        

