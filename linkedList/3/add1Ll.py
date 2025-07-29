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

def add1Ll(head:ListNode):
    if head == None:
        return ListNode(1)
    head = reverseList(head)
    pointer = head
    carry = 1
    while pointer != None and carry != 0:
        sum = pointer.val + carry
        carry = int(sum/10)
        sum = sum % 10
        pointer.val = sum
        pointer = pointer.next
    if carry == 1 and pointer == None:
        return ListNode(carry,head)
    return reverseList(head)

array = [1,2,3,4]
linked_list = convertToLL(array)
addition = add1Ll(linked_list)
traversal(addition)