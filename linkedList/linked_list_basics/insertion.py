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

def insertAtHead(head:Node, value):
    # temp = Node(value)
    # temp.next = head
    # head = temp
    # return head
    return Node(value,head)

def insertAtTail(head:Node, value):
    if head == None:
        return Node(value)
    pointer = head
    while pointer.next != None:
        pointer = pointer.next
    pointer.next = Node(value)
    return head

def insertion(head:Node,position,value):
    if head == None:
        if position == 1:
            return Node(value,head)
    if position == 1:
        return Node(value,head)
    pointer = head
    counter = 1
    temp = Node(value)
    while pointer.next != None:
        if counter == position - 1 :
            # temp.next = pointer.next
            # pointer.next = temp
            # return head
            break
        pointer = pointer.next
        counter += 1
    if counter == position - 1:
        temp.next = pointer.next
        pointer.next = temp
    return head

def insertBefore(head:Node,value,position):
    if head.data == position:
        return Node(value,head)
    pointer = head
    while pointer.next != None:
        if pointer.next.data == position:
            temp = Node(value)
            temp.next = pointer.next
            pointer.next = temp
            break
        pointer = pointer.next
    return head

array = [1,2,3,4,5]
linked_list = convertToLL(array)
linked_list = insertBefore(linked_list,9,0)
traversal(linked_list)