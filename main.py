from lds import Stack


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


def main():
    stack_opeartions()
    # reverse_word()


if __name__ == '__main__':
    main()