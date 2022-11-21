from tools import measure_execution_time


class PriorityQueue:
    def __init__(self):
        self.array = []
    
    @property
    def __size(self):
        return len(self.array)

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

    def __str__(self) -> str:
        return f'{self.array}'