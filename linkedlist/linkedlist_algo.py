
from linkedlist.singly_linked_list import SinglyLinkedList,Node

#Reverse singly-linked list
#Note that input is assumed to be a Node,not a linked list
def reverse(head:Node):
    p = head
    reversed_head = None
    while p:
        next= p._next
        p._next = reversed_head
        reversed_head = p
        p = next
    return reversed_head

def has_circle(head:Node):
    slow = fast = head
    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next
        if slow == fast:
            return True
    return False

def print_all(head: Node):
    nums = []
    current = head
    while current:
        nums.append(current._data)
        current = current._next
    print("->".join(str(num) for num in nums))

def merge(head1:Node,head2:Node):
    p1,p2 = head1,head2
    p = fake_head = Node(1)
    while p1 and p2:
        if p1._data <= p2._data:
            p._next = p1
            p1 = p1._next
        else:
            p._next = p2
            p2 = p2._next
        p = p._next
    p._next = p1 if p1 else p2
    return fake_head._next

def nth_node(head:Node,n):
    p1 = p2 = head
    position = 0
    while p2 and position < n:
        p2 = p2._next
        position += 1
    while p2:
        p1 = p1._next
        p2 = p2._next
    return p1

def find_middle_node(head:Node):
    slow = fast = head
    while fast and fast._next:
        slow = slow._next
        fast = fast._next._next
    return slow



