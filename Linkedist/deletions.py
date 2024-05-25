class Box:
    def __init__(self, data):
        self.data = data 
        self.next = None
def deleteHeadNodeInLinkedList(head):
    if head == None:
	    return None 
    secondNode = head.next 
    head.next = None 
    return secondNode 
 
def deleteNodeAtSpecificPosition(head, position):
    if position == 0:
        return deleteHeadNodeInLinkedList(head)
 
    currentIndex = 0 
    currentNode = head 
    while currentIndex != position - 1:
        currentIndex += 1 
        currentNode = currentNode.next 
 
    nodeToBeDeleted = currentNode.next 
    currentNode.next = nodeToBeDeleted.next 
    nodeToBeDeleted.next = None 
    return head
 
 
head = None
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for ele in nums:
    head = insertAtBeginning(head, ele)
 
printLinkedList(head)
head = deleteNodeAtSpecificPosition(head, 5)
printLinkedList(head)