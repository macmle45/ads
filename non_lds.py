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
    

class TreeNode:
    def __init__(self, value) -> None:
        self.value = value
        self.left_child = None
        self.right_child = None


class TreeTraversal:
    def inorder(self, root):
        if root:
            self.inorder(root.left_child)
            print(str(root.value) + '->', end='')
            self.inorder(root.right_child)

    def preorder(self, root):
        if root:
            print(str(root.value) + '->', end='')
            self.preorder(root.left_child)
            self.preorder(root.right_child)

    def postorder(self, root):
        if root:
            self.postorder(root.left_child)
            self.postorder(root.right_child)
            print(str(root.value) + '->', end='')


class BinaryTree:
    def isFullTree(self, root):
        if root is None:
            return True
        
        if root.left_child is None and root.right_child is None:
            return True
        
        if root.left_child is not None and root.right_child is not None:
            return (self.isFullTree(root.left_child) and self.isFullTree(root.right_child))

        return False


class PerfectBinaryTree:
    def calculateDepth(self, node):
        depth = 0

        while node is not None:
            depth += 1
            node = node.left_child
        
        return depth

    def is_perfect(self, root, depth, level=0):
        # check if the tree is empty
        if root is None:
            return True

        # check the presence of trees
        if root.left_child is None and root.right_child is None:
            return (depth == level + 1)

        if root.left_child is None or root.right_child is None:
            return False

        return self.is_perfect(root.left_child, depth, level + 1) and self.is_perfect(root.right_child, depth, level + 1)


class CompleteBinaryTree:
    def count_nodes(self, root):
        if root is None:
            return 0
        return (1 + self.count_nodes(root.left_child) + self.count_nodes(root.right_child))

    def is_complete(self, root, index, number_nodes):
        if root is None:
            return True
        
        if index >= number_nodes:
            return False

        return self.is_complete(root.left_child, 2 * index + 1, number_nodes) and self.is_complete(root.right_child, 2 * index + 2, number_nodes)
         

class TreeHeight:
    def __init__(self) -> None:
        self.height = 0

class BalancedBinaryTree:
    def isHighhtBalanced(self, root: TreeNode, height: TreeHeight):
        left_height = TreeHeight()
        right_height = TreeHeight()

        if root is None:
            return True

        l = self.isHighhtBalanced(root.left_child, left_height)
        r = self.isHighhtBalanced(root.right_child, right_height)

        height.height = max(left_height.height, right_height.height) + 1

        if abs(left_height.height - right_height.height) <= 1:
            return l and r

        return False


class BinarySearchTree:
    def __init__(self, data) -> None:
        self.root = None

        for val in data:
            self.root = self.insert(self.root, val)
            

    def insertNode(self, node: TreeNode, val):
        if node is None:
            return TreeNode(val)
        
        if val < node.value:
            node.left_child = self.insert(node.left_child, val)
        else:
            node.right_child = self.insert(node.right_child, val)

        return node


    def deleteNode(self, root: TreeNode, val):
        if root is None:
            return root

        if val < root.value:
            root.left_child = self.deleteNode(root.left_child, val)
        elif val > root.value:
            root.right_child = self.deleteNode(root.right_child, val)
        else:
            if root.left_child is None:
                temp = root.right_child
                root = None
                return temp
            elif root.right_child is None:
                temp = root.left_child
                root = None
                return temp


        


    def preorder_traverse(self, root: TreeNode):
        if root is not None:
            print(str(root.value) + ' ->', end=' ')
            self.preorder_traverse(root.left_child)
            self.preorder_traverse(root.right_child)

        
            
