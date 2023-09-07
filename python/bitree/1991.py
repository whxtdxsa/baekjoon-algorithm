class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:
    def __init__(self, value):
        self.root = Node(value)

    def insert(self, p_v, l_v, r_v):
        self._insert_recursive(self.root, p_v, l_v, r_v)

    def _insert_recursive(self, node, value, l_v, r_v):
        if value == node.value:
                node.left = Node(l_v)
                node.right = Node(r_v)
        elif value > node.value:
            if node.left != None: self._insert_recursive(node.left, value, l_v, r_v)
            if node.right != None: self._insert_recursive(node.right, value, l_v, r_v)
    
    def preorder_traversal(self):
        self._preorder_traversal_recursive(self.root)

    def _preorder_traversal_recursive(self, node):
        if node != None:
            if node.value != ".": print(node.value, end='')
            self._preorder_traversal_recursive(node.left)
            self._preorder_traversal_recursive(node.right)

    def inorder_traversal(self):
        self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, node):
        if node != None:
            self._inorder_traversal_recursive(node.left)
            if node.value != ".": print(node.value, end='')
            self._inorder_traversal_recursive(node.right)

    def postorder_traversal(self):
        self._postorder_traversal_recursive(self.root)

    def _postorder_traversal_recursive(self, node):
        if node != None:
            self._postorder_traversal_recursive(node.left)
            self._postorder_traversal_recursive(node.right)
            if node.value != ".": print(node.value, end='')

t = Tree("A")
for _ in range(int(input())):
    p_v, l_v, r_v = input().split(" ")
    t.insert(p_v, l_v, r_v)
t.preorder_traversal()
print()
t.inorder_traversal()
print()
t.postorder_traversal()
