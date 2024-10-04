from listaDuplamenteEncadeadas import DoublyLinkedList

# Definição da classe Stack usando a lista duplamente encadeada
class Stack:
    def __init__(self):
        self._list = DoublyLinkedList()  # Internamente, a pilha usa uma lista duplamente encadeada

    # Método para empilhar (push)
    def push(self, data):
        self._list.append(data)  # Insere no final da lista (cauda)

    # Método para desempilhar (pop)
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        top_data = self._list.tail.data  # Obtém o valor no topo (cauda)
        self._list.remove_at(self._list.size() - 1)  # Remove o último nó (cauda)
        return top_data

    # Método para visualizar o topo (peek)
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._list.tail.data  # Retorna o valor no topo (cauda)

    # Método para verificar se a pilha está vazia
    def is_empty(self):
        return self._list.size() == 0

    # Método para obter o tamanho da pilha
    def size(self):
        return self._list.size()

    # Método para exibir a pilha (do topo para o fundo)
    def print_stack(self):
        self._list.print_backward()  # Exibe da cauda (topo) até a cabeça (fundo)
