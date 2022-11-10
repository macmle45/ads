from lds import Stack, Queue, CircularQueue


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


def main():
    # stack_opeartions()
    # reverse_word()
    # queue_operations()
    circular_queue_operations()


if __name__ == '__main__':
    main()