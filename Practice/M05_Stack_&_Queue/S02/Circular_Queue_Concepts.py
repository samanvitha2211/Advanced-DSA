size = 5
li = [None] * size
print(li)

class Circular_Queue:
    def __init__(self,size):
        self.size = size
        self.queue = [None]*self.size
        self.front = -1
        self.rear = -1

    def enqueue(self,data):
        pass