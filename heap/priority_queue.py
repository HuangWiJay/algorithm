class QueueNode:
    def __init__(self,priority,data=None):
        assert type(priority) is int and priority >= 0
        self.priority = priority
        self.data = data

class PriorityQueue:
    def __init__(self,capacity = 100):
        self._capacity = capacity
        self._q = []
        self._length = 0

    def enqueue(self,priority,data = None):
        if self._length >= self._capacity:
            return False
        new_node = QueueNode(priority,data)
        self._q.append(new_node)
        self._length += 1

        nn = self._length - 1
        while nn >0:
            p = (nn - 1) // 2
            if self._q[nn].priority < self._q[p].priority:
                self._q[nn],self._q[p] = self._q[p],self._q[nn]
                nn = p
            else:
                break
        return True

    def dequeue(self):
        if self._length <= 0:
            return False

        self._q[0],self._q[-1] = self._q[-1],self._q[0]
        ret = self._q.pop()
        self._length -= 1

        if self._length > 1:
            lp = (self._length - 2) // 2
            idx = 0

            while idx <= lp:
                lc = 2 * idx + 1
                rc = lc + 1

                if rc <= self._length - 1:
                    tmp = lc 
