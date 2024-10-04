from stack import Stack

# Testando a implementação da pilha
stack = Stack()

# Inserindo elementos na pilha
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("Pilha após empilhar elementos (do topo para o fundo):")
stack.print_stack()

# Visualizando o topo da pilha
print("\nElemento no topo:", stack.peek())

# Removendo elementos da pilha
print("\nDesempilhando:", stack.pop())
print("Desempilhando:", stack.pop())

print("\nPilha após desempilhar dois elementos:")
stack.print_stack()

# Verificando o tamanho e se a pilha está vazia
print("\nTamanho da pilha:", stack.size())
print("A pilha está vazia?", stack.is_empty())

# Esvaziando a pilha completamente
stack.pop()
stack.pop()

print("\nPilha após esvaziar:")
print("A pilha está vazia?", stack.is_empty())
