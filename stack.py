class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return 'value: {0}, next: {1}'.format(self.value, self.next)


class Stack:

    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def push(self, value):
        node = Node(value, None)

        if self.length == 0:
            self.top = node
            self.bottom = node
            self.length += 1
            return node

        top = self.top
        node.next = top
        self.top = node
        self.length += 1

    def pop(self):
        if self.length == 0:
            raise Exception('Stack is empty')

        if self.length == 1:
            self.bottom = None

        top = self.top
        self.top = top.next
        top = None

        self.length -= 1

        return top

    def peek(self):
        if self.length == 0:
            raise Exception('Stack is empty')
        return self.top


stack = Stack()
stack.push(10)
stack.push(15)
stack.push(20)
stack.pop()
print(stack.peek())
