class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def add(self, data):
        new_node = Node(data)
        if self.next is None:
            self.next = new_node
        else:
            current = self.next
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self
        while current is not None:
            print(current.data)
            current = current.next

# Create a linked list and add some nodes
head = Node(1)
head.add(2)
head.add(3)
head.display()  # Output: 1 2 3
