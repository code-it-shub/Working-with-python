class Node:
    def __init__(self,value,left=None,right=None):
        self.value = value
        self.left =left
        self.right = right


class BinraryTree:
    def __init__(self):
        self.head = None
        self.level = 0

    def insertion(self,root,key):
        if root is None:
            root=Node(key)
        elif key > root.value:
            root.right = self.insertion(root.right,key)
        else:
            root.left=self.insertion(root.left,key)    
        return root
    def printTree(self,root):
        if root:
            print(f"|--{root.value}--|")
            print("\n")
            self.printTree(root.right)
            self.printTree(root.left)
        else:
            print("none")

    def InOrderTraversal(self,root):
        if root:
            self.InOrderTraversal(root.left)
            print(root.value)
            self.InOrderTraversal(root.right)
        else:
            return
    def preOrderTraversal(self,root):
        if root:
            print(root.value)
            self.preOrderTraversal(root.left)
            self.preOrderTraversal(root.right)
        else:
            return
    def search(self,root,key):
        if root.value == key:
            print(f"Key Found on level {self.level}")
        elif key > root.value:
            self.level = self.level +1
            self.search(root.right,key)
        else:
            self.level = self.level +1
            self.search(root.left,key)
        return ValueError




bt=BinraryTree()
n=Node(10)
bt.insertion(n,23)
bt.insertion(n,1)
bt.insertion(n,33)
bt.insertion(n,3)
bt.insertion(n,34)
bt.insertion(n,6)
bt.insertion(n,8)
bt.search(n,34)