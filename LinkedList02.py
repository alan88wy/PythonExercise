class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
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
        print("Add ->", value)

    def pop_first(self):
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
        print("Pop First ->", temp.value)
        return temp.value

    def pop_last(self):
        if self.head is None:
            return None

        temp = self.head
        pre = self.head

        if self.length == 1:
            val = self.head.value
            self.head = None
            self.tail = None
        else:
            while temp.next:
                pre = temp
                temp = temp.next
            val = temp.value
            self.tail = pre
            self.tail.next = None

        self.length -= 1
        print("Pop Last ->", val)
        return val

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        print("Prepend ->", value)

    def get(self, index):
        if index < 0 or index >= self.length:
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next

        print(f"Get Index {index} -> {temp.value}")
        return temp

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            print(f"Set Index {index} -> {value}")
            return True
        return False

    def insert(self, index, value):
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
        print(f"Insert Index {index} -> {value}")
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_last()

        prev = self.get(index - 1)
        removed = prev.next
        prev.next = removed.next
        self.length -= 1
        print(f"Remove Index {index} -> {removed.value}")
        return removed.value

    def reverse(self):
        prev = None
        current = self.head
        self.tail = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        print("Linked List Reversed")

    def display(self):
        current = self.head
        li = []
        while current:
            li.append(current.value)
            current = current.next
        print("Current list ->", li)


# ===========================
# ✅ TEST CASES
# ===========================

linked_list = LinkedList(1)
linked_list.display()   # [1]

linked_list.add(2)
linked_list.display()   # [1, 2]

linked_list.add(3)
linked_list.display()   # [1, 2, 3]

linked_list.pop_first()   # Removes 1
linked_list.display()     # [2, 3]

linked_list.pop_last()    # Removes 3
linked_list.display()     # [2]

linked_list.prepend(0)    # Adds 0 at start
linked_list.display()     # [0, 2]

linked_list.set_value(1, 5)  # Sets index 1 → 5
linked_list.display()        # [0, 5]

linked_list.remove(1)     # Removes index 1 (5)
linked_list.display()     # [0]

linked_list.insert(1, 10)  # [0, 10]
linked_list.display()

linked_list.insert(2, 6)   # [0, 10, 6]
linked_list.display()

linked_list.insert(1, 4)   # [0, 4, 10, 6]
linked_list.display()

linked_list.reverse()      # [6, 10, 4, 0]
linked_list.display()
