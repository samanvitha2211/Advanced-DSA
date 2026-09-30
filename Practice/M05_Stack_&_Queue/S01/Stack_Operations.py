class Stack:
    def __init__(self):
        self.s = []
    def push(self, val):
        self.s.append(val)

    def is_empty(self):
        if len(self.s) == 0:
            return True 
        else:
            return False
        
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        return self.s.pop()
    def size(self):
        return len(self.s)
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return self.s[-1]
        
st = Stack()
print(st.is_empty())
st.push(10)
st.push(20)
st.push(30)
print(st.is_empty())
print(st.pop())
print(st.size())
print(st.peek())
#Stack implementation using Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack_LL:
    def __init__(self):
        self.top = None
    def push(self,val):
        new_node = Node(val)
        new_node.next = self.top 
        self.top = new_node
    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False 
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        del_val = self.top.data
        self.top = self.top.next
        return del_val 
    
    def size(self):
        count = 0
        temp = self.top 
        while temp:
            count += 1
            temp = temp.next
        return count
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.top.data
obj2 = Stack_LL()
print(obj2.is_empty())
obj2.push(40)
obj2.push(50)
obj2.push(60)
obj2.push(70)
print(obj2.is_empty())
print(obj2.pop())
print(obj2.size())
print(obj2.peek())