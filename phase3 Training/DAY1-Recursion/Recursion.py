# calling a fun again and again

#printing 1 to n
def fun(i,n):
    if(i<=n):
        print(i)
        fun(i+1,n)
n=int(input())
i=1
fun(i,n)


#printing n to 1
def fun(n):
    if(n!=0):
        print(n)
        fun(n-1)
n=int(input())
fun(n)


#printing 'n' odd numbers
def fun(n,i):
    if(i%2!=0 and i<=n):
        print(i)
        fun(n,i+1)
    elif(i>n):
       return
    else:
       fun(n,i+1) 
    
n=int(input())
i=1
fun(n,i)


#RECURSION EXAMPLE 1
def p(i,n):
    if i>=n:
        print("base condition got hit")
        return
    print("hlo",i)
    print("world",i)
    p(i+1,n)
    print("this",i)
    print("is a recursion",i)
p(1,8)

#RECURSION EXAMPLE 2
def printT(i,n):
    if i>=n:
        print("base condition got hit")
        return
    print("ending",i)
    for j in range(1,i):
        print(j)
    printT(i+1,n)
    print("starting",i)
printT(1,8)

#RECURSION EXAMPLE 3
def printT(pos):
    print("leaving here",pos)
    if pos==0:
        print("base condition got hit")
        return
    if pos%2==1:
        print("even pos",pos)
    else:
        print("odd pos",pos)
    printT(pos-1)
    for j in range(pos,-1,-1):
        print("index",j)
    print("entering here",pos)
printT(11)






