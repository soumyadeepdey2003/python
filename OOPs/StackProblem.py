class Stack:
    def __init__(self):
        self.list=[]
       
    def push(self,e):
        self.list.append(e)

    # def pop(self):
    #     if len(self.list) == 0:
    #         print("nothing to pop")
    #     else:
    #         print(self.list.pop())

    def pop(self):
        n = len(self.list)
        if n == 0:
            print("nothing to pop")
            return
        
        print(self.list[n-1])
        del self.list[n-1]
        
    def display(self):
        print("display")
        for x in reversed(self.list):
            print(x)

s1=Stack()
s1.push(15)
s1.push(1)
s1.push(14)
s1.push(13)
s1.push(11)
s1.display()
print("pop")
s1.pop()
s1.pop()
s1.display()