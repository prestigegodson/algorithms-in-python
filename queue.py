class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return 'value: {0}, next: {1}'.format(self.value, self.next)


class Queue:

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def enqueue(self, value):
        node = Node(value, None)

        if self.length == 0:
            self.first = node
            self.last = node
            self.length += 1
            return node

        last = self.last
        last.next = node
        self.last = node
        self.length += 1

    def dequeue(self):
        if self.length == 0:
            raise Exception('Stack is empty')

        value = None
        if self.first == self.last:
            value = self.first.value
            self.first = None
            self.last = None
            self.length = 0
            return value

        value = self.first.value
        first = self.first
        self.first = first.next
        self.length -= 1

        return value

    def peek(self):
        return self.first
