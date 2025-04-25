class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None: 
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)

    def _insert_recursive(self, current_node, data):
        if current_node.data > data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:

            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)

    def posterior_traversal(self):
        self._posterior_traversal_recursive(self.root)

    def _posterior_traversal_recursive(self, current_node):
        if current_node is not None:
            self._posterior_traversal_recursive(current_node.left)
            self._posterior_traversal_recursive(current_node.right)
            print(current_node.data)

import sys
sys.setrecursionlimit(10**5)
bt = BinaryTree()
while True: 
    try: 
        n = sys.stdin.readline().rstrip()
        if not n: break
        bt.insert(int(n))
    except EOFError:
        break

bt.posterior_traversal()

