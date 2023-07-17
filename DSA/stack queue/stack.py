class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=next
class stack:
    def __init__(self):
        self.top=None
        self.size= 0

    def push(self,value):
        newNode=Node(value)
        if self.top is None:
            self.top = newNode
            self.size = self.size +1
        else:
            curr= self.top
            while curr.next:
                curr=curr.next
                self.size = self.size+1

            self.top=curr