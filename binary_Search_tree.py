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




bst = BinarySearchTree()
bst.insert(9)
bst.insert(4)
bst.insert(20)
bst.insert(1)        
print(bst.lookup(4))
