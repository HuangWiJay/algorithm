class CircularQueue:
    def __init__(self,capacity):
        self._capacity = capacity + 1
        self._data = []
        self._head = 0
        self._tail = 0
    def enqueue(self,value):
        if (self._tail + 1) % self._capacity == self._head:
            return False
        if len(self._data) <= self._tail:
            self._data.append(value)
        else:
            self._data[self._tail] = value
        self._tail = (self._tail+1) % self._capacity
        return True

    def dequeue(self):
        if self._tail != self._head:
            value = self._head
            self._head = (self._head+1) % self._capacity
            return value

    def __repr__(self) -> str:
        if self._tail >= self._head:
            return " ".join(item for item in self._data[self._head : self._tail])
        else:
            from itertools import chain
            return " ".join(item for item in chain(self._data[self._head:], self._data[:self._tail]))

if __name__ == "__main__":
    q = CircularQueue(5)
    for i in range(5):
        q.enqueue(str(i))
    q.dequeue()
    q.dequeue()
    q.enqueue(str(0))
    q.enqueue(str(1))
    print(q)