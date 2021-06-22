import random


def quick_sort(l, r):
    if l >= r - 1:
        return
    d = (random.randint(l, r - 1))
    md = arr[d]
    i, j = l, r - 1
    while i <= j:
        while i < r and arr[i] < md:
            i += 1
        while j >= l and arr[j] > md:
            j -= 1
        if i <= j:
            t = arr[i]
            arr[i] = arr[j]
            arr[j] = t
            i += 1
            j -= 1
    quick_sort(l, i)
    quick_sort(i, r)


arr = [1, 3, 19, 14, 2, 10, 2, 1, -10, 1000, 0, -119]
quick_sort(0, len(arr))
print(arr)
