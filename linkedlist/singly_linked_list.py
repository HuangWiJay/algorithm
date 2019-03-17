class Node():
    def __init__(self,value,next=None):
        self._data = value
        self._next = next

class SinglyLinkedList:
    def __init__(self):
        self._head = None

    def __repr__(self):
        nums = []
        p = self._head
        while p:
            nums.append(p._data)
            p = p._next
        return " ".join(str(num) for num in nums)

    def __iter__(self):
        p = self._head
        while p:
            yield p._data
            p = p._next

    def insert_value_to_tail(self,value):
        new_node = Node(value)
        self.insert_node_to_tail(new_node)

    def insert_node_to_tail(self,new_node):
        if not self._head:
            self._head = new_node
            return True
        p = self._head
        while p._next:
            p = p._next
        p._next = new_node
        return True

    def insert_value_to_head(self,value):
        new_node = Node(value)
        self.insert_node_to_head(new_node)

    def insert_node_to_head(self,new_node):
        new_node._next = self._head
        self._head = new_node
        return True

    def insert_value_by_index(self,index,value):
        new_node = Node(value)
        self.insert_node_by_index(index,new_node)

    def insert_node_by_index(self,index,new_node):
        if index <= 0:
            self.insert_node_to_head(new_node)
            return True
        position = 0
        p = self._head
        while p._next and position < index - 1:
            p = p._next
            position += 1
        new_node._next = p._next
        p._next = new_node
        return True

    def find_by_value(self,value):
        p =self._head
        while p and p._data != value:
            p = p._next
        return p

    def find_by_index(self,index):
        position = 0
        p = self._head
        while p and position < index:
            p = p._next
            position += 1
        return p

    def delete_by_node(self,node):
        if not node:
            return False
        if node._next:
            node._data = node._next._data
            node._next = node._next._next
            return True
        p = self._head
        while p and p._next != node:
            p = p._next
        if not p:
            return False
        p._next = None

    def delete_by_value(self,value):
        pass

    def insert_value_after(self,node,value):
        new_node = Node(value)
        self.insert_node_after(node,new_node)

    def insert_node_after(self,node,new_node):
        if not node or not new_node:
            return False
        new_node._next = node._next
        node._next = new_node
        return True

    def insert_value_before(self,node,value):
        new_node = Node(value)
        self.insert_node_before(node,new_node)

    def insert_node_before(self,node,new_node):
        if not node or not new_node:
            return False
        if self._head == Node:
            self.insert_node_to_head(new_node)
            return True
        p = self._head
        while p and p._next != node:
            p = p._next
        if not p:
            return False
        new_node._next = node
        p._next = new_node
        return True

def reverse(singlyLinkedList):
    head = singlyLinkedList._head
    reversed_head = None
    while head:
        next = head._next
        head._next = reversed_head
        reversed_head = head
        head = next
    return reversed_head

if __name__ == '__main__':
    l = SinglyLinkedList()
    for i in range(15):
        l.insert_value_to_tail(i)
    print(l)
    node9 = l.find_by_value(9)
    l.insert_value_before(node9, 20)
    print(l)
    l.insert_value_after(node9, 16)
    node3 = l.find_by_index(3)
    l.delete_by_node(node3)
    l.delete_by_node(l._head)
    print(l)
    reverse(l)
    print(l)