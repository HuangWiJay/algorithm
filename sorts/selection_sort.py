def selection_sort(a:list):
    length = len(a)
    if length <= 1:
        return
    for i in range(length-1):
        min_value = a[i]
        min_index = i
        for j in range(i+1,length-i-1):
            if a[j] < min_value:
                min_value = a[j]
                min_index = j
        a[i],a[min_index] = min_value,a[i]


if __name__ == '__main__':
    import time,random
    a = []
    for i in range(8000):
        a.append(random.randint(0,80000)+(30 if i%3 ==0 else 0))
    start = time.time()
    selection_sort(a)
    end = time.time()
    print('耗时：%f'% (end-start))
    print(a)
