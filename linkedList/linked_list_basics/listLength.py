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

array = [1,2,3,4,5]
linked_list = convertToLL(array)
print(getLength(linked_list))