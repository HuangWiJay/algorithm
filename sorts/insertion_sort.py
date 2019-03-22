def insertion_sort(a:list):
    length = len(a)
    if length <= 1:
        return
    for i in range(1,length):
        value = a[i]
        j = i -1
        while j >= 0 and a[j] > value:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = value

if __name__ == '__main__':
    import time,random
    a = []
    for i in range(8000):
        a.append(random.randint(0,80000)+(30 if i%3 ==0 else 0))
    start = time.time()
    insertion_sort(a)
    end = time.time()
    print('耗时：%f'% (end-start))
    print(a)

