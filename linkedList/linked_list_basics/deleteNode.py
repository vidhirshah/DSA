class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def convertToLL(array):
    if len(array) == 0:
        return None
    head = Node(array[0])
    pointer = head
    for i in range(1,len(array)):
        temp = Node(array[i])
        pointer.next = temp
        pointer = pointer.next
    return head

def traversal(head :Node):
    pointer = head
    while pointer != None:
        print(pointer.data)
        pointer = pointer.next
    return

def getLength(head:Node):
    length = 0
    pointer = head
    while pointer != None:
        length += 1
        pointer = pointer.next
    return length

def removeHead(head:Node):
    if head == None:
        return None
    head = head.next
    return head

def removeTail(head:Node):
    if head == None or head.next == None:
        return None
    pointer = head
    while pointer.next.next != None:
        pointer = pointer.next
    pointer.next = None
    return head

def deleteKthEls(head:Node,k):
    if head == None:
        return None
    if k == 1:
        head = head.next
        return head
    counter = 1
    pointer = head
    while counter < k - 1 and pointer.next.next != None:
        pointer = pointer.next
        counter += 1
    if counter + 1 == k:
        pointer.next = pointer.next.next
    return head

array = [1,2,3,4,5]
linked_list = convertToLL(array)
linked_list = deleteKthEls(linked_list,4)
traversal(linked_list)