class Box:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def levelorder(root):
    if(root==None):
        return
    
    result=[] 
    queue=[root] 
    while(len(queue)>0):
        n=len(queue)
        subres=[]
        for i in range(n):
            
            #step1
            node=queue.pop(0)
            #step2
            subres.append(node.data)
            
            #step3
            if(node.left):
                queue.append(node.left)
            if(node.right):
                queue.append(node.right)
        result.append(subres)
    return result  
    
obj1=Box(40)
obj2=Box(30)
obj3=Box(20)
obj4=Box(50)
obj5=Box(60)
obj6=Box(80)
obj1.left=obj2
obj1.right=obj3
obj2.left=obj4
obj2.right=obj5
obj3.left=obj6
print(levelorder(obj1))