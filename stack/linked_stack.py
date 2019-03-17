from linkedlist.singly_linked_list import Node
class LinkedStack():
    def __init__(self,next = None):
        self.top = None

    def __repr__(self):
        p = self.top
        nums = []
        while p:
            nums.append(p._data)
            p = p._next
        return " ".join(str(num) for num in nums)

    def push(self,value):
        new_node = Node(value)
        new_node._next = self.top
        self.top = new_node
        return True

    def pop(self):
        top = self.top
        self.top = self.top._next
        return top

if __name__ == "__main__":
    stack = LinkedStack()
    for i in range(9):
        stack.push(i)
    print(stack)
    print('-' * 10)
    for _ in range(3):
        stack.pop()
    print(stack)