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

def reverseList(head:ListNode):
    current = head
    prev = None
    while current != None:
        front = current.next
        current.next = prev
        prev = current
        current = front
    return prev

def reverseKGroup(head:ListNode,k):
    if head == None or head.next == None:
        return head
    pointer = head
    first = head
    last = head
    count = 0
    lasttail= None
    while pointer != None:
        count += 1
        if count == k:
            count = 0
            last = pointer
            pointer = pointer.next
            last.next = None
            last = reverseList(first)
            if head == first:
                head = last
                lasttail = first
            lasttail.next = last
            lasttail = first
            first.next = pointer
            first = pointer
        else:
            pointer = pointer.next
    return head


array = [1,2,3,4,5]
linked_list = convertToLL(array)
reversed_list = reverseKGroup(linked_list,4)
traversal(reversed_list)