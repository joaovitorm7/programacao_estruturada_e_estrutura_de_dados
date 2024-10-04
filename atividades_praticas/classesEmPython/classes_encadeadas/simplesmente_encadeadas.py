class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
           
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def insert_at_beginning(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def get(self, possition):
        current = self.head
        index = 0
        while current:
            if index == possition:
                return current.data
            index += 1
            current = current.next
        raise IndexError("Position out of range")
        
    ##def remove(self, data):
        
    def remove_at_beginning(self):
        if self.head:
           old_head = self.head
           self.head = self.head.next
           self.head.next = None

    def display(self):
        current = self.head
        if not current:
            print("A lista está vazia")
        else:
            while current:
                print(current.data, "->")
                current = current.next
            print("None")
        
ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(3)
ll.insert_at_end(20)
ll.insert_at_beginning(5)
ll.display()

print("Valor na posição 2:", ll.get(0)) 
