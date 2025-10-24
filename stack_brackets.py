class Stack:
    def __init__(self):
        self.items = []

    def Push(self, data):
        self.items.append(data)

    def Pop(self):
        if not self.is_empty():
            return self.items.pop() 
        else:
            return None
    
    def is_empty(self):
        return len(self.items) == 0 
    
def isValid(expression):
    s = Stack()
    for i in exp:
        if i in '({[':
            s.Push(i)

        elif i in ')}]':
            last = s.Pop()
            if last is None:
                return False
            elif last == '(' and i == ')':
                continue
            elif last == '{' and i == '}':
                continue
            elif last == '[' and i == ']':
                continue
            else:
                return False
    return s.is_empty()

exp = input("Enter a string:")
if isValid(exp):
    print("The brackets are balanced!")
else:
    print("The brackets are NOT balanced.")