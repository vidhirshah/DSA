class Node():
    def __init__(self,data,next=None,back =None):
        self.data = data
        self.next = next
        self.back = back

def convertToLL(array):
    head = Node(array[0])
    pointer = head
    for i in range(1,len(array)):
        temp = Node(array[i],None,pointer)
        pointer.next = temp
        pointer = pointer.next
    return head

def traversal(head:Node):
    pointer = head
    while pointer != None:
        print(pointer.data)
        pointer = pointer.next
    return

def insertAtHead(head:Node,value):
    if head == None:
        return Node(value,None,None)
    temp = Node(value,head,None)
    head.back = temp
    return temp

def insertBeforeTail(head:Node,value):
    if head == None:
        return Node(value,None,None)
    if head.next == None:
        return insertAtHead(dll_list,value)
    tail = head
    while tail.next != None:
        tail = tail.next
    prev = tail.back
    temp = Node(value,tail,prev)
    prev.next = temp
    tail.back = temp
    return head

def insertAfterTail(head:Node,value):
    if head == None:
        return Node(value,None,Node)
    tail = head
    while tail.next != None:
        tail = tail.next
    temp = Node(value,None,tail)
    tail.next = temp
    return head

array = [1,2,3,4,5]
dll_list = convertToLL(array)
dll_list = insertAfterTail(dll_list,100)
traversal(dll_list)