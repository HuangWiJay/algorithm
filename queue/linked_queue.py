from linkedlist.singly_linked_list import Node
class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,value):
        node = Node(value)
        if not self.head:
            self.head = self.tail = node
        else:
            self.tail._next = node
            self.tail = node

    def dequeue(self):
        if self.head:
            head = self.head
            self.head = self.head._next
            if not self.head:
                self.tail = None
            return head

    def __repr__(self) -> str:
        values = []
        p = self.head
        while p:
            values.append(p._data)
            p = p._next
        return "->".join(value for value in values)

if __name__ == "__main__":
    q = LinkedQueue()
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("7")
    q.enqueue("8")
    print(q)