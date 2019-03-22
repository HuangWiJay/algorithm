def bubble_sort(a:list):
    length = len(a)
    if length <= 1:
        return a
    for i in range(length-1):
        made_swap = False
        for j in range(length-i-1):
            if a[j] > a[j+1]:
                a[j+1],a[j] = a[j],a[j+1]
                made_swap = True
        if not made_swap:
            break


if __name__ == '__main__':
    import time,random
    a = []
    for i in range(8000):
        a.append(random.randint(0,80000)+(30 if i%3 ==0 else 0))
    start = time.time()
    bubble_sort(a)
    end = time.time()
    print('耗时：%f'% (end-start))
    print(a)



