from _collections import deque

stack = deque()
print("Stack before pushes:")
print(stack)

stack.append('a')
stack.append('b')
stack.append('c')

print("\nStack after pushes:")
print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\nStack after pops:")
print(stack)

string = 'abc'
print(len(string))
print(string[1:len(string)-1])

