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

def getCarry(head:ListNode):
    if head == None:
        return 1
    sum = head.val + getCarry(head.next)
    carry = int(sum/10)
    sum = sum % 10
    head.val = sum
    return carry

def add1Ll(head:ListNode):
    carry = getCarry(head)
    if carry:
        return ListNode(carry,head)
    return head

array = [9,9,9,9]
linked_list = convertToLL(array)
addition = add1Ll(linked_list)
traversal(addition)