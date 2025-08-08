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

def duplicates(head:Node):
    if head == None or head.next == None:
        return head
    pointer = head.next
    while pointer != None:
        if pointer.back.data == pointer.data:
            prev = pointer.back
            prev.next = pointer.next
            if pointer.next.back:
                pointer.next.back = pointer.back
            pointer.next = None
            pointer.back = None
            pointer = prev.next
        else:
            pointer = pointer.next
    return head

array = [1,1,1,3]
dll_list = convertToLL(array)
ans = duplicates(dll_list)
traversal(ans)