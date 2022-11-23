from tools import measure_execution_time


class Heap:
    def __init__(self, max_heap=True) -> None:
        self.__max_heap = max_heap
        self.array = []

    @property
    def size(self) -> int:
        return len(self.array)
    
    @property
    def peak(self):
        """
        Peak: return root node from min-heap/max-heap
        """
        return self.array[0]

    def heapify(self, i):
        # largest/smallest index
        largest = i
        smallest = i

        # left child index
        left = 2 * i + 1

        # right child index
        right = 2 * i + 2


        if self.__max_heap:
            if left < self.size and self.array[left] > self.array[largest]:
                largest = left

            if right < self.size and self.array[right] > self.array[largest]:
                largest = right

            # swap current element with smallest 
            if largest != i:
                self.array[i], self.array[largest] = self.array[largest], self.array[i]
                self.heapify(largest)
        else:
            if left < self.size and self.array[left] < self.array[largest]:
                smallest = left

            if right < self.size and self.array[right] < self.array[largest]:
                smallest = right

            # swap current element with smallest 
            if smallest != i:
                self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
                self.__heapify(smallest)


class PriorityQueue:
    def __init__(self):
        self.heap = Heap()

    @property
    def peek(self):
        return self.heap.peak
    
    @property
    def extract(self):
        """
        Extract-Max: return the node with maximum value after removing it from a Max Heap
        Extract-Min: return the node with minimum value after removing it from a Min Heap
        """
        rootNode = self.heap.array[0]
        self.removeNode(rootNode)

        return rootNode

    # insert new element to the queue
    def insert(self, new_node: int):
        if self.heap.size == 0:
            self.heap.array.append(new_node)
        else:
            self.heap.array.append(new_node)

            # heapify (from the last element)
            for i in range((self.heap.size // 2) - 1, -1, -1):
                self.heap.heapify(i)

    # delete element from the priority queue
    def removeNode(self, ntbd):
        # init index
        i = 0

        # find index of node to be deleted
        for i in range(0, self.heap.size):
            if ntbd == self.heap.array[i]:
                break
        
        # swap ntbd with last element
        self.heap.array[i], self.heap.array[self.heap.size - 1] = self.heap.array[self.heap.size - 1], self.heap.array[i]

        # delete last element
        self.heap.array.remove(self.heap.array[self.heap.size - 1])

        # heapify tree
        for i in range((self.heap.size // 2) - 1, -1, -1):
            self.heap.heapify(i)

    def __str__(self) -> str:
        return f'{self.heap.array}'
    
