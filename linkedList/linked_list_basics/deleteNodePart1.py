class ListNode():
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def convertToLL(array):
    if len(array) == 0:
        return None
    head = ListNode(array[0])
    pointer = head
    for i in range(1,len(array)):
        temp = ListNode(array[i])
        pointer.next = temp
        pointer = pointer.next
    return head

def traversal(head :ListNode):
    pointer = head
    while pointer != None:
        print(pointer.val)
        pointer = pointer.next
    return

def getLength(head:ListNode):
    length = 0
    pointer = head
    while pointer != None:
        length += 1
        pointer = pointer.next
    return length

def deleteNode(head:ListNode,k):
    if head == None:
        return None
    if head.val == k:
        head = head.next
        return head
    prev  = head
    current = prev.next
    while current != None:
        if current.val == k:
            prev.next = current.next
            current.next = None
            return head
        prev = current
        current = current.next
    return head

array = [1,2,3,4,5]
linked_list = convertToLL(array)
linked_list = deleteNode(linked_list,4)
traversal(linked_list)