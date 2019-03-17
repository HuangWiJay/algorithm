
class MyArray:
    def __init__(self,capacity):
        self._capacity = capacity
        self._count = 0
        self._data = []

    def __getitem__(self, item):
        if item < self._count and item >= -self._count:
           return self._data[item]

    def __repr__(self):
        return ' '.join(str(num) for num in self._data[:self._count])

    def _is_full(self):
        if self._count == self._capacity:
            return True
        return False

    def insert_to_tail(self,value):
        if self._is_full():
            return False
        self._data.append(value)
        self._count += 1
        return True

    def insert_to_head(self,value):
        if self._is_full():
            return False
        if self._count == 0:
            self._data.append(value)
            self._count += 1
            return True
        else:
            self._data[1:self._count+1] = self._data[:self._count]
            self._data[0] = value
            self._count += 1
            return True

    def insert_v2(self,index,value):
        if self._is_full():
            return False
        if index >= self._count:
            self.insert_to_tail(value)
        elif index <= 0:
            self.insert_to_head(value)
        else:
            self._data[index+1:self._count+1] = self._data[index:self._count]
            self._data[index] = value
        self._count += 1
        return True

    def delete(self,index):
        if index < -self._count or index >= self._count:
            return False

        value = self._data[index]
        self._data[index:self._count-1] = self._data[index+1:self._count]
        self._count -= 1
        self._data = self._data[:self._count]
        return value


if __name__ == "__main__":
    a = MyArray(6)
    for i in range(6):
        a.insert_to_tail(i)
    a.delete(2)
    print(a)
    a.insert_to_tail(7)
    print(a)
    print('origin', a)
    a.delete(4)
    print('delete ', a)