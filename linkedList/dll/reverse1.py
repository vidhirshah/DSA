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

def reverse(head:Node):
    current = head
    prev = current.back
    while current != None:
        front = current.next
        current.back = current.next
        current.next = prev
        prev = current
        current = front
    head = prev
    return head

array = [1,2,3,4,5]
dll_list = convertToLL(array)
dll_list = reverse(dll_list)
traversal(dll_list)