class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.empty():
            return self.stack.pop()
        return -1
    def peek(self):
        if not self.empty():
            return self.stack[-1]
        return -1
    
    def empty(self):
        return True if len(self.stack) == 0 else False
    
    def size(self):
        return len(self.stack)
    
N = int(input())

stack = Stack()

for _ in range(N):
    command = input().split()
    if command[0] == 'push':

        stack.push(command[1])
    elif command[0] == 'pop':
        print(stack.pop())

    elif command[0] == 'top':
        print(stack.top())
        
    elif command[0] == 'size':
        print(stack.size())
    elif command[0] == 'empty':
        print(stack.empty())