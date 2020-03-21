class Stack:
    def __init__(self,size=100):
        self.size=size
        self.stack=[]
        self.top=-1
    def push(self,x):# 入栈之前检查栈是否已满
        if self.isfull():
            raise Exception("stack is full")
        else:
            self.stack.append(x)
            self.top=self.top+1

    def pop(self):# 出栈之前检查栈是否为空
        if self.isempty():
            raise Exception("stack is empty")
        else:
            self.top=self.top-1
            self.stack.pop()

    def isfull(self):
        return self.top+1 == self.size
    def isempty(self):
        return self.top == '-1'
    def showStack(self):
        print(self.stack)
    def showStack_as_str(self):
        s="".join(self.stack)
        return s