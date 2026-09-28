'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.prev = node1

node2.next = node3
node3.prev = node2

node3.next = node4
node4.prev = node3

def travarse_forward():
    curr = node1
    while curr:
        print(curr.data, end = "<->")
        curr = curr.next
    print("None")
travarse_forward()

def travarse_backward():
    curr = node4
    while curr:
        print(curr.data, end = "<->")
        curr = curr.prev
    print("None")
travarse_backward()
'''


'''
 # Insertion in the beginning

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
def insert_begin(head,data):
    new_node = Node(data)
    new_node.next = head
    if head:
        head.prev = new_node
    return new_node
def traverse(head):
    curr = head
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.next
    print("None")
head = None
head = insert_begin(head, 50)
head = insert_begin(head, 60)
head = insert_begin(head, 70)
print("Insertion at the Begin")
traverse(head)
print()


def insert_end(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = new_node
    new_node.prev = curr.next
    return head
def traverse(head):
    curr = head
    while curr:
        print(curr.data, end = " <-> ")
        curr = curr.next
    print("None")
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class Double_LL:
    def __init__(self):
        self.head = None
    def insert_begin(self, data):
        new_node = Node(data)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head == None:
            return new_node
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr

    def delete_gegin(self):
        if self.head is None:
            return
        del_node = self.head
        self.head = self.head.next
        del del_node
    def delete_end(self):
        if self.head is None:
            return

    
    def count_nodes(self):
        if self.head is None:
            return 0
        if self.head.next is None:
            return 1
        temp = self.head
        count = 0
        while temp:
            count += 1
            temp = temp.next
        return count
    
    def traverse(self):
        if self.head is None:
            return
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")
    

dll = Double_LL()

dll.insert_begin(10)
dll.insert_end(20)

dll.traverse()
