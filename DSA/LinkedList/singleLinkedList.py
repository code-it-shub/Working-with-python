class Node:
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None
    
    def printLL(self):
        if self.head is None:
            print('Linked List empty')
        else:
            n=self.head
            while n is not None:
                print(n.data)
                n = n.next

    def insertion(self,value):
        newNode = Node(value)     
        if self.head:
            currentNode=self.head
            while currentNode.next:
                currentNode=currentNode.next
            currentNode.next=newNode
        else:
            self.head=newNode

    def deletion(self):
        if self.head is None:
            return ValueError
        elif self.head.next is None:
            self.head = None
            return 
        else:
            curr=self.head
            while curr.next is not None:
                prev=curr
                curr=curr.next  
            prev.next=None
            curr=None
            return prev

        
    def deletionWithKey(self,key):
        if self.head is None:
            return ValueError
        elif self.head == key:
            self.head = None
            return 
        else:
            curr = self.head
            prev=self.head 
            curr=curr.next
            if curr.data == key:
                prev.next=curr.next
                curr=None
                return 
            prev.next = curr
            while curr.next:
                if curr.data == key:
                    break    
                curr=curr.next
                prev=prev.next
            prev.next=curr.next
            curr=None
            return
            


            

        

LL=LinkedList()
LL.insertion(212)
LL.insertion(44)
LL.insertion(4)
LL.insertion(4)
LL.insertion(4)
LL.insertion(2)
LL.deletionWithKey(4)
LL.printLL()



        
