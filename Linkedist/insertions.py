class Box():
    def __init__(self,ele):
        self.ele=ele
        self.next=None
def printLinkedList(head):
    while(head!=None):
        print(head.ele)
        head=head.next
def insertionAtEnd(head,ele):
    temp=Box(ele)
    if(head==None):
        return temp
    tail=head
    while(tail.next!=None):
        tail=tail.next
    tail.next=temp
    return head
def insertionAtBegining(head,ele):
    temp=Box(ele)
    if(head==None):
        return temp
    temp.next=head
    return temp

def insertAtSpecificPosition(head, position, ele):
    if position == 0:
        return insertAtBeginning(head, ele)
 
    temp = Box(ele)
    currentIndex = 0 
    currentNode = head 
    while currentIndex != position - 1:
        currentIndex += 1 
        currentNode = currentNode.next 
 
    temp.next = currentNode.next 
    currentNode.next = temp 
    return head
    

head=None
l=[10,20,30,40,50]
for i in l:
    head=insertionAtEnd(head,i)
printLinkedList(head)