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

def rotateRight(head:ListNode,k):
    if head == None or head.next == None or k == 0:
        return head
    count = 0
    pointer = head
    first = head
    while pointer.next != None:
        count += 1
        pointer = pointer.next
    pointer.next = head
    k %=  count
    if k == 0:
        return head
    k = count - k
    count = 0
    pointer = head
    while pointer.next != None:
        count += 1
        if count == k:
            last = pointer
            pointer = pointer.next
            break
        pointer = pointer.next
    
    head = last.next
    last.next = None
    return head

array = [1,2,3,4,5]
linked_list = convertToLL(array)
reversed_list = rotateRight(linked_list,2)
traversal(reversed_list)