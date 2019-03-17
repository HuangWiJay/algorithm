'''
Insertion,deletion and random access of array
Assumes int for element type
The beauty of data structures and algorithms
'''

from typing import Optional

class MyArray:
    """
    A simple wrapper around List
    You can't have -1 in the array
    """

    def __init__(self,capacity: int):
        self._data = []
        self._count = 0
        self._capacity = capacity

    def __getitem__(self, position: int) -> int:
        """
        Support for subscript
        Perhaps better than the find() method below
        """
        return self._data[position]

    def find(self,index: int) -> Optional[int]:
        if index >= self._count or index <= -self._count:
            return None
        return self._data[index]

    def delete(self,index: int) -> bool:
        if index >= self._count or index <= -self._count:
            return False

        self._data[index:-1] = self._data[index+1:]
        self._count -= 1
        #真正将数据删除并覆盖原来的数据
        self._data = self._data[:self._count]
        print('delete function',self._data)
        return True

    def insert_v2(self,index: int,value: int) -> bool:
        """
        支持任意位置插入
        :param index:
        :param value:
        :return:
        """
        if self._capacity == self._count:
            return False
        if index >= self._count:
            self._data.append(value)
        elif index <0 :
            self._data.insert(0,value)
        else:
            self._data[index+1:self._count+1] = self._data[index:self._count]
            self._data[index] = value
        self._count+= 1
        return True

    def __repr__(self):
        return " ".join(str(num) for num in self._data[:self._count])


    def insert_to_tail(self,value: int) -> bool:
        if self._count == self._capacity:
            return False
        if self._count == len(self._data):
            self._data.append(value)
        else:
            self._data[self._count] = value
        self._count += 1
        return True

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
