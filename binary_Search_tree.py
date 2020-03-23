from queue import Queue


class Node:

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        """
        Returning a json format string without the enclosing curly braces{}
        """
        left = self.left if self.left else ''
        right = self.right if self.right else ''
        return '"value": {0}, "left": {{ {1} }}, "right": {{ {2} }}'.format(self.value, left, right)


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, value):

        if not self.root:
            self.root = Node(value, None, None)
            return self.root

        next_tree = self.root

        while True:
            if next_tree.value <= value:
                if not next_tree.right:
                    next_tree.right = Node(value, None, None)
                    break
                else:
                    next_tree = next_tree.right
            else:
                if not next_tree.left:
                    next_tree.left = Node(value, None, None)
                    break
                else:
                    next_tree = next_tree.left

    def lookup(self, value):

        next_tree = self.root

        while True:
            if not next_tree:
                return None
            elif next_tree.value == value:
                return next_tree
            elif value < next_tree.value:
                next_tree = next_tree.left
            else:
                next_tree = next_tree.right

    def breadth_first_search(self):
        array = []
        queue = Queue()
        current_node = self.root
        queue.enqueue(current_node)

        while queue.length > 0:
            current_node = queue.dequeue()
            array.append(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

        return array

    def dfs_in_order(self):
        return BinarySearchTree._traverse_in_order(self.root, [])

    def dfs_pre_order(self):
        return BinarySearchTree._traverse_pre_order(self.root, [])

    def dfs_post_order(self):
        return BinarySearchTree._traverse_post_order(self.root, [])

    @staticmethod
    def _traverse_pre_order(node, array):
        array.append(node.value)

        if node.left:
            BinarySearchTree._traverse_pre_order(node.left, array)

        if node.right:
            BinarySearchTree._traverse_pre_order(node.right, array)

        return array

    @staticmethod
    def _traverse_in_order(node, array):

        if node.left:
            BinarySearchTree._traverse_in_order(node.left, array)

        array.append(node.value)

        if node.right:
            BinarySearchTree._traverse_in_order(node.right, array)

        return array

    @staticmethod
    def _traverse_post_order(node, array):

        if node.left:
            BinarySearchTree._traverse_post_order(node.left, array)

        if node.right:
            BinarySearchTree._traverse_post_order(node.right, array)

        array.append(node.value)

        return array


bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(6)
bst.insert(20)
bst.insert(170)
bst.insert(15)
bst.insert(1)
print(bst.breadth_first_search())
print(bst.dfs_pre_order())
print(bst.dfs_in_order())
print(bst.dfs_post_order())
"""
            9
    4               20
1        6       15        170
BFS[9, 4, 20, 1, 6, 15, 170]
"""
