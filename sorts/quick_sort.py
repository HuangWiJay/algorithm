import random
def quick_sort(a:list):
    _quick_sort_between(a,0,len(a) - 1)
def _quick_sort_between(a:list,low:int,high:int):
    if low >= high:
        return
    k = random.randint(low,high)
    a[low],a[k] = a[k],a[low]
    m = _partition(a,low,high)
    _quick_sort_between(a,low,m-1)
    _quick_sort_between(a,m+1,high)

def _partition(a:list,low:int,high:int):
    pivot,j = a[low],low
    for i in range(low+1,high+1):
        if a[i] <= pivot:
            j += 1
            a[j],a[i] = a[i],a[j]
    a[low],a[j] = a[j],a[low]
    return j


if __name__=='__main__':
    import time,random
    a = []
    for i in range(8000):
        a.append(random.randint(0,80000)+(30 if i%3 ==0 else 0))
    start = time.time()
    quick_sort(a)
    end = time.time()
    print('耗时：%f'% (end-start))
    print(a)