def merge_sort(l, r):
    if r - l <= 1:
        return
    d = (l + r) // 2
    merge_sort(l, d)
    merge_sort(d, r)
    ll, rr = l, d
    sorted = []
    while ll < d or rr < r:
        if ll != d and (rr == r or arr[ll] <= arr[rr]):
            sorted.append(arr[ll])
            ll += 1
        else:
            sorted.append(arr[rr])
            rr += 1
    for i in range(l, r):
        arr[i] = sorted[i - l]


arr = [1, 3, 19, 14, 2, 10, 2, 1, -10, 1000, 0]
merge_sort(0, len(arr))
print(arr)
