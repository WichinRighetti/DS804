'''
Implemente una de las siguientes tres estructuras de datos en python (Pilas, colas. árboles) con las
siguientes funciones básicas:
• agregar
• eliminar
• buscar
'''

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._add_recursive(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._add_recursive(node.right, value)

    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                min_node = self._find_min(node.right)
                node.value = min_node.value
                node.right = self._delete_recursive(node.right, min_node.value)

        return node

    def _find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node

        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)


tree = BinarySearchTree()
tree.add(50)
tree.add(30)
tree.add(70)
tree.add(20)
tree.add(40)
tree.add(60)
tree.add(80)

print(tree.search(30))  # Output: <__main__.Node object at 0x...>
print(tree.search(70)) 
print(tree.search(80)) 
print(tree.search(50)) 
print(tree.search(90))  # Output: None

tree.delete(30)
print(tree.search(30))  # Output: None
