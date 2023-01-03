from lds import (
                    Stack, 
                    Queue, 
                    CircularQueue,  
                    Deque,
                    LinkedList,
                    DoubleLinkedList,
                    HashTable
                )

from non_lds import (
                    PriorityQueue, 
                    TreeNode, 
                    TreeTraversal, 
                    BinaryTree, 
                    PerfectBinaryTree,
                    CompleteBinaryTree,
                    TreeHeight,
                    BalancedBinaryTree
                )

import random


def stack_opeartions():
    my_stack = Stack()
    
    print(my_stack.pop())
    print(f"Is empty: {my_stack.is_empty()}")
    my_stack.push(1)
    print(my_stack.pop())
    print(f"Stack: {my_stack}")
    print(f"Is empty: {my_stack.is_empty()}")
    my_stack.pop()
    print(f"Is empty: {my_stack.is_empty()}")
    my_stack.push(3)
    my_stack.push(10)
    my_stack.push(5)
    my_stack.push(7)
    print(f"Stack: {my_stack}")
    print("Removing last item...")
    my_stack.pop()
    print(f"Stack: {my_stack}")

    print(f"Peek: {my_stack.peek()}")


def reverse_word():
    word = 'ala ma kota'
    reversed_word = ''

    stack_word = Stack()

    for letter in word:
        stack_word.push(letter)

    for _ in word:
        reversed_word += f'{stack_word.pop()}'

    print(reversed_word)


def queue_operations():
    my_queue = Queue()

    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)

    print(f"Current queue: {my_queue}")
    print(f"Size: {my_queue.size}\n")


    print(f'Dequeue element: {my_queue.dequeue()}\nQueue: {my_queue}')
    print(f"Size: {my_queue.size}\n")

    print(f'Dequeue element: {my_queue.dequeue()}\nQueue: {my_queue}')
    print(f"Size: {my_queue.size}\n")

    print(f'Dequeue element: {my_queue.dequeue()}\nQueue: {my_queue}')
    print(f"Size: {my_queue.size}\n")

    print(f'Dequeue element: {my_queue.dequeue()}\nQueue: {my_queue}')
    print(f"Size: {my_queue.size}\n")


def circular_queue_operations():
    cq = CircularQueue(5)

    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)

    print(f'Initial circular queue...\n{cq}')

    cq.dequeue()

    print(f'After dequeue...\n{cq}')

    cq.enqueue(6)

    print(f'After enqueue...\n{cq}')

    print(f'{cq.dequeue()}')
    cq.enqueue(7)

    print(cq)

    print(f'{cq.dequeue()}')
    cq.enqueue(8)

    print(cq)


def priority_queue_operations():
    pq = PriorityQueue()

    pq.insert(1)
    pq.insert(2)
    pq.insert(3)
    pq.insert(4)
    pq.insert(5)
    pq.insert(9)

    print(f"Init queue...\n{pq}\n")

    pq.insert(7)
    print(f'Queue after insert (7) operation: {pq}\n')

    pq.removeNode(3)
    print(f'Queue after delete (3) operation: {pq}\n')

    print(f'Peek: {pq.peek}\n')

    print(f'Extract: {pq.extract}\n')

    print(f'Peek: {pq.peek}\n')

    print(f'Queue after extract (Max-Heap) operation: {pq}\n')


def deque_operations():
    my_deque = Deque()

    my_deque.addFront(1)
    my_deque.addFront(2)
    my_deque.addRear(4)

    print(f'Deque init...\n{my_deque}\n')

    my_deque.removeFront()
    print(f'Deque after deleting from front: {my_deque}\n')

    my_deque.removeRear()
    print(f'Deque after deleting from rear: {my_deque}\n')


def linked_list_operations():
    linked_list = LinkedList()

    # linked_list.insert_front(1)
    # linked_list.insert_front(2)
    # linked_list.insert_front(3)
    # linked_list.insert_front(4)
    # linked_list.insert_front(5)

    for _ in range(0,10000):
        linked_list.insert_front(random.randint(0, 9))

    # print(f'Init linked list...\n{linked_list}\n')
    
    # linked_list.insert_middle(7, 2)
    # print(f'Insert element 7 at index 2\n{linked_list}\n')

    # linked_list.insert_middle(3, 2)
    # print(f'Insert element 3 at index 2\n{linked_list}\n')

    # linked_list.insert_middle(5, 2)
    # print(f'Insert element 5 at index 2\n{linked_list}\n')

    # linked_list.insert_middle(9, 2)
    # print(f'Insert element 9 at index 2\n{linked_list}\n')

    # linked_list.insert_middle(11, 3)
    # print(f'Insert element 11 at index 3\n{linked_list}\n')

    # linked_list.delete_front()
    # print(f'Delete element at front\n{linked_list}\n')

    # linked_list.delete_rear()
    # print(f'Delete element from rear\n{linked_list}\n')

    # linked_list.delete_middle(1)
    # print(f'Delete element at index 1\n{linked_list}\n')
    
    # linked_list.insert_middle(11, 1)
    # print(f'Insert element 11 at index 1\n{linked_list}\n')

    # linked_list.insert_middle(5, 2)
    # print(f'Insert element 5 at index 2\n{linked_list}\n')

    # linked_list.insert_middle(9, 4)
    # print(f'Insert element 9 at index 4\n{linked_list}\n')

    # print(f'Linked list length: {linked_list.length}\n')

    # print(f'Searching element 56: {linked_list.search_list(56)}\n')
    # print(f'Searching element 11: {linked_list.search_list(11)}\n')

    # print(f'Sorted:\n{linked_list}\n')
    # print(linked_list.get_index(5))

    linked_list.sort_list()

    print(linked_list)
    


def double_linked_list_operations():
    double_linked_list = DoubleLinkedList()

    double_linked_list.insert_front(1)
    double_linked_list.insert_front(2)
    double_linked_list.insert_front(3)

    print(double_linked_list)


def hash_table_operations():
    # add removing from hash table

    my_hash_table = HashTable(6)

    my_hash_table.insert(123, 'Red Bull')
    my_hash_table.insert(456, 'Ferrari')
    my_hash_table.insert(375, 'Mercedes')
    my_hash_table.insert(291, 'Alpine')
    my_hash_table.insert(571, 'McLaren')
    my_hash_table.insert(658, 'Aston')

    print(my_hash_table)


def tree_traversal():
    # create tree
    root = TreeNode(1)
    root.left_child = TreeNode(2)
    root.right_child = TreeNode(3)
    root.left_child.left_child = TreeNode(4)
    root.left_child.right_child = TreeNode(5)

    travers = TreeTraversal()

    print('Inorder')
    travers.inorder(root)

    print('\n\nPreorder')
    travers.preorder(root)

    print('\n\nPostorder')
    travers.postorder(root)


def binary_tree_ops():
    root = TreeNode(1)

    root.left_child = TreeNode(2)
    root.right_child = TreeNode(3)

    root.left_child.left_child = TreeNode(4)
    root.left_child.right_child = TreeNode(5)

    root.left_child.right_child.left_child = TreeNode(6)
    root.left_child.right_child.right_child = TreeNode(7)

    bt = BinaryTree()

    is_full_tree = bt.isFullTree(root)

    print(is_full_tree)


def perfect_binary_tree_ops():
    root = TreeNode(1)
    root.left_child = TreeNode(2)

    pbt = PerfectBinaryTree()

    tree_depth = pbt.calculateDepth(root)

    result = pbt.is_perfect(root, tree_depth)

    print(result)


def complete_binary_tree_ops():
    # create complete binary tree
    root = TreeNode(1)

    root.left_child = TreeNode(2)
    root.right_child = TreeNode(3)
    
    root.left_child.left_child = TreeNode(4)
    root.left_child.right_child = TreeNode(5)

    root.left_child.left_child.left_child = TreeNode(7)
    root.left_child.left_child.right_child = TreeNode(8)

    root.left_child.right_child.left_child = TreeNode(9)
    root.left_child.right_child.right_child = TreeNode(10)

    root.right_child.left_child = TreeNode(6)
    root.right_child.right_child = TreeNode(12)

    root.right_child.left_child.left_child = TreeNode(11)
    root.right_child.left_child.right_child = TreeNode(13)

    root.right_child.right_child.left_child = TreeNode(14)
    
    # ops
    cbt = CompleteBinaryTree()

    nodes_number = cbt.count_nodes(root)
    print(f'Nodes number: {nodes_number}')

    index = 0
    tree_is_complete = cbt.is_complete(root, index, nodes_number)
    print(f'Tree is complete: {tree_is_complete}')


def balanced_binary_tree_ops() :
    height = TreeHeight()
    root = TreeNode(1)

    root.left_child = TreeNode(2)
    root.right_child = TreeNode(3)

    root.left_child.left_child = TreeNode(4)
    root.left_child.right_child = TreeNode(5)

    root.left_child.right_child.left_child = TreeNode(6)

    bbt = BalancedBinaryTree()

    is_balanced = bbt.isHighhtBalanced(root, height)

    print(f'The tree is balanced: {is_balanced}')


def main():
    # stack_opeartions()
    # reverse_word()
    # queue_operations()
    # circular_queue_operations()
    # priority_queue_operations()
    # deque_operations()
    # linked_list_operations()
    # double_linked_list_operations()
    # hash_table_operations()
    # tree_traversal()
    # binary_tree_ops()
    # perfect_binary_tree_ops()
    # complete_binary_tree_ops()
    balanced_binary_tree_ops()
    # pass


if __name__ == '__main__':
    main()