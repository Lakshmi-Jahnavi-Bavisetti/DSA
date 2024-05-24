class Box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def printpostorder(root):
    if root==None:
        return
    printinorder(root.left)
    printinorder(root.right)
    print(root.data,end=" ")
obj1=Box(50)
obj2=Box(40)
obj3=Box(60)
obj1.left=obj2 
obj1.right=obj3
printinorder(obj1)
print()
printpostorder(obj1)
print()
printpreorder(obj1) 