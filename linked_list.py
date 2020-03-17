class LinkedListNode:

    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return 'value: {0}, next: {1}'.format(self.value, self.next)


class LinkedList:

    def __init__(self, value):
        head = LinkedListNode(value, None)
        self.head = head
        self.tail = head
        self.length = 1

    def append(self, value):
        tail = LinkedListNode(value, None)
        self.tail.next = tail
        self.tail = tail
        self.length += 1

        return tail

    def prepend(self, value):
        head = LinkedListNode(value, self.head)
        self.head = head
        self.length += 1

        return head

    def print_list(self):
        array = []
        current_node = self.head

        while current_node:
            array.append(current_node.value)
            current_node = current_node.next

        return array

    def insert(self, index, value):

        if index >= self.length or index < 0:
            raise IndexError('linked list index {0} out of bound'.format(index))

        if index == 0:
            return self.prepend(value)

        leader = self.head
        counter = 0

        while counter < index-1:
            leader = leader.next
            counter += 1

        next_node = leader.next
        node = LinkedListNode(value, next_node)
        leader.next = node
        self.length += 1

        return node

    def delete(self, index):

        if index >= self.length or index < 0:
            raise IndexError('linked list index {0} out of bound'.format(index))

        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return

        if index == 0:
            head = self.head
            self.head = head.next
            return

        leader = self.head
        counter = 0

        while counter < index-1:
            leader = leader.next
            counter += 1

        node_to_delete = leader.next
        leader.next = node_to_delete.next

        self.length -= 1

    def __str__(self):
        return 'Head= {0}, length= {1}'.format(self.head, self.length)
