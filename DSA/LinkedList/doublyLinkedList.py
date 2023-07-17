class Node:
    def __init__(self,data,next=None,prev=None):
        self.data= data
        self.next= next
        self.prev= prev

class LinkedList:
    def __init__(self):
        self.head  = None
        self.tail = None
    
    def pushTail(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            curr= self.head
            while curr.next:
                curr=curr.next
            curr.next=newNode
            self.tail=newNode

    def pushHead(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail= newNode
        else:
            newNode.next = self.head
            self.head = newNode

    def printLL(self):
        curr=self.head 
        if self.head is None:
            print("linkedList is empty")
        else:
            while curr.next is not None:
                print(curr.data)
                curr=curr.next
            print(curr.data)
    





    
LL = LinkedList()

LL.pushHead(23)
LL.pushHead(33)
LL.pushHead(55)
LL.pushTail(1)
LL.pushTail(2)
LL.printLL()