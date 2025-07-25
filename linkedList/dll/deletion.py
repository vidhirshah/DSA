class Node():
    def __init__(self,data,next=None,back=None):
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

def deleteHead(head:Node):
    if head == None or head.next == None:
        return None
    temp = head
    head = head.next
    head.back = None
    temp.next = None
    return head

def deleteTail(head:None):
    if head == None or head.next == None:
        return None
    pointer = head
    while pointer.next != None:
        pointer = pointer.next
    prev = pointer.back
    prev.next = None
    pointer.back = None
    return head

def deleteKthEls(head:Node,position):
    if head == None:
        return None
    counter = 1
    current = head
    while current.next != None:
        if counter == position:
            break
        counter += 1
        current = current.next
    prev = current.back
    front = current.next
    if prev == None and front == None:
        return None
    elif prev == None:
        return deleteHead(head)
    elif front == None:
        return deleteTail(head)
    prev.next = front
    current.next = None
    front.back = prev
    current.back = None
    return head

def deleteByValue(head:Node,key):
    if head == None:
        return None
    counter = 1
    current = head
    while current != None:
        if counter == key:
            break
        counter += 1
        current = current.next
    if current != None:
        prev = current.back
        front = current.next
        if prev == None and front == None:
            return None
        elif prev == None:
            return deleteHead(head)
        elif front == None:
            return deleteTail(head)
        prev.next = front
        current.next = None
        front.back = prev
        current.back = None
    return head

array = [1,2,3,4,5]
dll_list = convertToLL(array)
dll_list = deleteByValue(dll_list,9)
traversal(dll_list)