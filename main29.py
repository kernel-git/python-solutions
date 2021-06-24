def gen(obj):
    if type(obj) is not list:
        yield obj
        return
    for item in obj:
        yield from gen(item)


# lst = [[1, 1], [2], [1, 1]]
lst = [[1, [1, 3]], 2, [1, 4, [6]]]
for i in gen(lst):
    print(i, end=" ")
