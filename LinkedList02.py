class Node():
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def add(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            
        self.length += 1

    def pop_first(self):
        # Pop the first item
        if self.head is None:
            return None
        
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            temp.next = None
            
        self.length -= 1
        return temp.value
    
    def pop_last(self):
        # Pop the last item
        if self.head is None:
            return None

        temp = self.head
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            while temp.next != self.tail:
                temp = temp.next
                
            self.tail = temp
            temp.next = None
            
        self.length -= 1
        return temp.value
    
    def prepend(self, value):
        # Prepend a new node
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1
    
    def get(self, index):
        # Get the value at a given index
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        return temp
    
    def set_value(self, index, value):
        # Set the value at a given index
        
        if index < 0 or index >= self.length:
            return False
        
        temp = self.get(index)
        
        # if temp is not None:
        if temp:
            temp.value = value
            return True
        
        return False
    
    def insert(self, index, value):
        # Insert a new node at a given index
        if index < 0 or index > self.length:
            return False
        
        if index == 0:
            self.prepend(value)
            return True
        
        if index == self.length:
            self.add(value)
            return True
        
        new_node = Node(value)
        
        temp = self.get(index - 1)
        
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        
        return True
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

# Create a linked list and add some nodes
linked_list = LinkedList(1)
linked_list.add(2)
linked_list.add(3)
linked_list.pop_first()  # Removes 1
linked_list.pop_last()   # Removes 3

linked_list.display()   # Output: 2

linked_list.prepend(0)  # Adds 0 at the beginning
linked_list.display()   # Output: 0 2

if not linked_list.set_value(1, 5):  # Sets the value at index 1 to 5
    print("Failed to set value")
linked_list.display()   # Output: 0 5


