class Queue:
    def __init__(self):
        self.list=[]
       
    def enqueue(self,e):
        self.list.append(e)

    def dequeue(self):
        n = len(self.list)
        if n == 0:
            print("nothing to pop")
            return
        print(self.list[0])
        self.list.pop(0)
        
    def display(self):
        print("display")
        for x in range(0,len(self.list)):
            print(self.list[x])

s1=Queue()
s1.enqueue(15)
s1.enqueue(1)
s1.enqueue(14)
s1.enqueue(13)
s1.enqueue(11)
s1.display()
print("dequeue")
s1.dequeue()
s1.dequeue()
s1.display()