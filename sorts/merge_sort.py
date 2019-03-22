def merge_sort(a:list):
    _merge_sort_between(a,0,len(a) - 1)

def _merge_sort_between(a:list,low:int,high:int):
    if low >= high:return
    mid = (low + high) // 2
    _merge_sort_between(a,low,mid)
    _merge_sort_between(a,mid+1,high)
    _merge(a,low,mid,high)



def _merge(a:list,low:int,mid:int,high:int):
    i,j = low,mid+1
    tmp = []
    while i <= mid and j <= high:
        if a[i] <= a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start:end+1])
    a[low:high+1] = tmp


if __name__=='__main__':
    import time,random
    a = []
    for i in range(8000):
        a.append(random.randint(0,80000)+(30 if i%3 ==0 else 0))
    start = time.time()
    merge_sort(a)
    end = time.time()
    print('耗时：%f'% (end-start))
    print(a)