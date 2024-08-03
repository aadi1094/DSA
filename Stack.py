
class Stack:
    def __init__(self):
        self.list=[]

    def __str__(self):
        values=self.list.reverse()
        values=[str(x) for x in self.list]
        return '\n'.join(values)

    #isEmpty
    def isEmpty(self):
        if self.list==[]:
            return True
        else:
            return False

    #Push
    def push(self,value):
        self.list.append(value)
        return "The elements inserted successfully"

    #Pop
    def pop(self):
        if self.isEmpty():
            return "There is no elements to pop from stack"
        else:
            return self.list.pop()

    #Peek
    def peek(self):
        if self.isEmpty():
            return "There are no elements"
        return self.list[-1]

customStack=Stack()
# print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
# print(customStack)
# print(customStack.isEmpty())
# print(customStack.pop())
print(customStack.peek())
print(customStack)
