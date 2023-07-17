class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self,value):
        newNode= Node(value)
        if self.head is None:
            self.head= newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.tail.next = newNode
            self.tail=newNode

    def printCll(self):
        if self.head is None:
            print("list is empty")
        else:            
            curr = self.head
            while curr is not self.tail:
                print(curr.data)
                curr=curr.next
            print(curr.data)


cll=CircularLinkedList()
cll.push(23)
cll.push(3)
cll.push(44)
cll.push(55)
cll.push(66)
cll.printCll()
