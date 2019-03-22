def shell_sort(a:list):
    length = len(a)
    if length <= 1:
        return
    gap = length // 2
    while gap >= 1:
        for j in range(gap,length):
            i = j
            while i-gap >= 0:
                if a[i] < a[i-gap]:
                    a[i],a[i-gap] = a[i-gap],a[i]
                    i -= gap
                else:
                    break
        gap //= 2


if __name__=='__main__':
    import time,random
    a = []
    for i in range(8000):
        a.append(random.randint(0,80000)+(30 if i%3 ==0 else 0))
    start = time.time()
    shell_sort(a)
    end = time.time()
    print('耗时：%f'% (end-start))
    print(a)

