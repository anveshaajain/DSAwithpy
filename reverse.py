def reverse_string(s):
    stack = list(s)
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    return reversed_str

print(reverse_string("hello"))
