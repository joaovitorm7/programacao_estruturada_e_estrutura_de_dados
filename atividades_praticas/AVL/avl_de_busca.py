class AVLTree:
    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right
            self.height = 1

    def __init__(self):
        self.root = None

    # Função para obter a altura do nó
    def _get_height(self, node):
        return node.height if node else 0

    # Função para calcular o fator de balanceamento
    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    # Função de rotação à direita
    def _right_rotate(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))
        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))

        return x

    # Função de rotação à esquerda
    def _left_rotate(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self._get_height(x.left), self._get_height(x.right))
        y.height = 1 + max(self._get_height(y.left), self._get_height(y.right))

        return y

    # Função de inserção
    def _insert(self, node, key):
        if not node:
            return self.Node(key)
        elif key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        # Verifica os casos de rotação
        if balance > 1 and key < node.left.key:
            return self._right_rotate(node)

        if balance < -1 and key > node.right.key:
            return self._left_rotate(node)
    
        if balance > 1 and key > node.left.key:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)
  
        if balance < -1 and key < node.right.key:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    # Método público de inserção
    def insert(self, key):
        self.root = self._insert(self.root, key)

    # Função para encontrar o menor valor em uma árvore
    def _get_min_value_node(self, node):
        if node is None or node.left is None:
            return node
        return self._get_min_value_node(node.left)

    # Função de remoção
    def _delete(self, node, key):
        if not node:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)

        # Verifica os casos de rotação
        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._right_rotate(node)

        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._left_rotate(node.left)
            return self._right_rotate(node)

        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._left_rotate(node)
        
        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._right_rotate(node.right)
            return self._left_rotate(node)

        return node

    # Método público de remoção
    def delete(self, key):
        self.root = self._delete(self.root, key)

    # Percurso em ordem (In-order)
    def in_order(self, node, result):
        if node:
            self.in_order(node.left, result)
            result.append(node.key)
            self.in_order(node.right, result)
        return result

    # Percurso pré-ordem (Pre-order)
    def pre_order(self, node, result):
        if node:
            result.append(node.key)
            self.pre_order(node.left, result)
            self.pre_order(node.right, result)
        return result

    # Percurso pós-ordem (Post-order)
    def post_order(self, node, result):
        if node:
            self.post_order(node.left, result)
            self.post_order(node.right, result)
            result.append(node.key)
        return result

avl = AVLTree()
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(40)
avl.insert(50)
avl.insert(25)

avl.delete(10)

print("In-order:", avl.in_order(avl.root, []))
print("Pre-order:", avl.pre_order(avl.root, []))
print("Post-order:", avl.post_order(avl.root, []))
