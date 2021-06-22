def merge_intervals(invervals, new_interval):
    ans = []
    up_left, up_right = None, None
    for interval in invervals:
        if interval[0] == new_interval[0] and interval[1] == new_interval[1]:
            return invervals
        if interval[0] > new_interval[1] or interval[1] < new_interval[0]:
            ans.append(interval)
            continue
        if interval[0] >= new_interval[0] and interval[1] <= new_interval[1]:
            continue
        if interval[0] <= new_interval[0] and interval[1] <= new_interval[1]:
            up_right = interval
        if interval[0] >= new_interval[0] and interval[1] >= new_interval[1]:
            up_left = interval
    if up_left is None and up_right is None:
        ans.append(new_interval)
    elif up_right is None:
        up_left[0] = new_interval[0]
        ans.append(up_left)
    elif up_left is None:
        up_right[1] = new_interval[1]
        ans.append(up_right)
    else:
        ans.append([up_right[0], up_left[1]])
    return ans

# arr = [int(item) for item in input("arr: ").split()]
# invervals = [[3, 5], [8, 10], [1, 2], [6, 7], [12, 16]]
# print(merge_intervals(invervals, [4, 8])) 7], [12, 16]]


invervals = [[6, 9], [1, 3]]
print(merge_intervals(invervals, [9, 31]))