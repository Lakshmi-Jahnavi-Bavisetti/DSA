def LeftView(root):
    if root==None:
        return[]
    resut=[]
    Q=[root]
    
    while Q:
        n=len(Q)
        for i in range(n):
            curr=Q.pop(0)
            if i==0:
                result.append(curr.data)
            if curr.left!=None:
                Q.append(curr.left)
            if curr.right:
                Q.append(curr.right)
    return result
