class ListNode():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def convertToLL(array):
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

def removeNthFromEnd(head:ListNode,n):
    length = 0
    pointer = head
    while pointer != None:
        length += 1
        pointer = pointer.next
    if length == n:
        pointer = head
        head = head.next
        pointer.next = None
        return head
    length -= n 
    counter = 1
    pointer = head
    while counter != length:
        pointer = pointer.next
        counter += 1
    temp = pointer.next
    pointer.next = temp.next
    temp.next = None
    return head

array = [1,2,3,4,5]
linked_list = convertToLL(array)
n = 2
reversed_list = removeNthFromEnd(linked_list,n)
traversal(reversed_list)