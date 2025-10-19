class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1] if self.items else None
    def is_empty(self):
        return len(self.items) == 0

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.peek())  # Output: 2
print(stack.is_empty())  # Output: False
print(stack.pop())  # Output: 2
print(stack.pop())  # Output: 1
print(stack.is_empty())  # Output: True
# print(stack.pop())  # Output: IndexError
print(stack.peek())  # Output: None
print(stack.is_empty())  # Output: True
# print(stack.pop())  # Output: IndexError

'''
List Methods:

Method	    Description
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	    Returns a copy of the list
count()	    Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	    Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	    Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	    Sorts the list
'''