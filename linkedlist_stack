class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

s = Stack()
s.push(5)
s.push(15)
print(s.pop())
print(s.peek())
print(s.is_empty())
