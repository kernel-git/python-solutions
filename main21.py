string = input()
arr = []

for val in string:
    if val == '{' or val == '(' or val == '[':
        arr.append(val)

    if val == '}' or val == ')' or val == ']':
        if len(arr) == 0:
            raise ValueError(f'{string[:string.find(val)]} > {string[string.find(val):]}')
        delee = arr.pop(len(arr) - 1)
        if not chr(ord(val) - 2) == delee and not chr(ord(val) - 1) == delee:
            raise ValueError(f'{string[:string.find(val)]} > {string[string.find(val):]}')

if not len(arr) == 0:
    raise ValueError(f'{string} <')
