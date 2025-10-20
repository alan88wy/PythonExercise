# Definition for singly-linked list.
'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:

        head = ListNode(0) # create dummy head
        current = head

        carry = 0

        while l1 is not None or l2 is not None or carry > 0:
            v1 = l1.val if l1 is not None else 0
            v2 = l2.val if l2 is not None else 0

            tot = v1 + v2 + carry

            carry = tot // 10
            remain = tot % 10

            current.next = ListNode(remain)
            current = current.next

            if l1 is not None:
                l1 = l1.next

            if l2 is not None:
                l2 = l2.next    

        return head.next

    def display(self, head: ListNode):
            current = head
            li = []
            while current:
                li.append(current.val)
                current = current.next
            print("Current list ->", li)
    
    def get_middle_node(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            
        return slow
    
    def check_loop(self, head: ListNode) -> bool:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
    
    def k_node_from_end(self, head: ListNode, k: int) -> ListNode:
        
        if head is None:
            return None
        
        slow = head
        fast = head

        # move fast to kth node to ensure slow and fast is always kth node apart
        for _ in range(k):
            if fast is None:
                return None
            fast = fast.next

        # move both slow and fast until fast reaches end
        while fast is not None:
            slow = slow.next
            fast = fast.next

        return slow
    
    def remove_duplicates(self, head: ListNode) -> ListNode:
        current = head

        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return head
    
list1 = [9,9,9,9,9,9,9, 9]
list2 = [9,9,9,9]

l1 = ListNode(0)
current = l1
for i in list1:
    current.next = ListNode(i)
    current = current.next

l1 = l1.next

l2 = ListNode(0)
current = l2
for i in list2:
    current.next = ListNode(i)
    current = current.next
    
l2 = l2.next

a = Solution()
b = a.addTwoNumbers(l1, l2)

a.display(b)

c = a.get_middle_node(b)
print("Middle Node ->", c.val)

d = a.check_loop(b)
print("Has Loop ->", d)

a.remove_duplicates(b)
a.display(b)