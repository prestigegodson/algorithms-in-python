class DoublyLinkedListNode:

    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
        return 'value: {0}, next: {1}, prev: {2}'.format(self.value, self.next, self.prev.value if self.prev else None)


class DoublyLinkedList:

    def __init__(self, value):
        head = DoublyLinkedListNode(value, None, None)
        self.head = head
        self.tail = head
        self.length = 1

    def append(self, value):
        tail = DoublyLinkedListNode(value, None, self.tail)
        self.tail.next = tail
        self.tail = tail
        self.length += 1

        return tail

    def prepend(self, value):
        head = DoublyLinkedListNode(value, self.head, None)
        self.head.prev = head
        self.head = head
        self.length += 1

        return head

    def print_list(self):
        array = []
        current_node = self.head

        while current_node:
            array.append({'value': current_node.value, 'previous': current_node.prev.value if current_node.prev else None})
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
        node = DoublyLinkedListNode(value, next_node, leader)
        next_node.prev = node
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
            self.head.prev = None
            return

        leader = self.head
        counter = 0

        while counter < index-1:
            leader = leader.next
            counter += 1

        node_to_delete = leader.next
        next_node = node_to_delete.next

        if next_node:
            next_node.prev = leader

        leader.next = next_node

        self.length -= 1

    def reverse(self):
        current = self.tail
        array = []

        while current:
            array.append(current.value)
            current = current.prev

        return array

    def __str__(self):
        return 'Head= {0}, length= {1}'.format(self.head, self.length)


linked_list = DoublyLinkedList(5)
linked_list.append(10)
linked_list.append(15)
linked_list.append(20)
print(linked_list.print_list())
print(linked_list.reverse())
