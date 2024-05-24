class Box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def zigzagordertraversal(root):
    if root==None:
        return
    Q=[root]
    result=[]
    level=0
    while(Q):
        n=len(Q)
        subresult=[]
        for i in range(n):
            curr=Q.pop()
            subresult.append(curr.data)
            if(curr.left):
                Q.append(curr.left)
            if(curr.right):
                Q.append(curr.right)
        if(level%2==1):
            subresult=subresult[::-1]
        level+=1
        result.append(subresult)
    return(result)
    
     
    
obj1=Box(40)
obj2=Box(30)
obj3=Box(20)
obj1.left=obj2
obj1.right=obj3
obj2.left=Box(90)
obj2.right=obj3
obj1.left=obj2
obj1.right=obj3
print(zigzagordertraversal(obj1))