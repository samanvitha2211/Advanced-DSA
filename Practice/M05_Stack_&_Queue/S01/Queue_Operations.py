class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,val):
        self.queue.append(val)
    def is_empty(self):
        return len(self.queue) == 0
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue.pop(0)
    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.queue[0]
    def display(self):
        if self.is_empty():
            return "Queue is empty"
        for ele in self.queue:
            print(ele,end=" ")

obj3 = Queue()
print(obj3.is_empty())
obj3.enqueue(10)
obj3.enqueue(20)
obj3.enqueue(30)
obj3.enqueue(40)
obj3.display()
print(obj3.is_empty())
print(obj3.dequeue())
print(obj3.front())