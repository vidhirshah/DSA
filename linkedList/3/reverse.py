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
    stack = []
    pointer = head
    while pointer != None:
        stack.append(pointer.val)
        pointer = pointer.next
    pointer = head
    while pointer != None and len(stack) > 0:
        pointer.val = stack.pop()
        pointer =pointer.next
    return head

array = [1,2,3,4,5,6]
linked_list = convertToLL(array)
reversed_list = reverseList(linked_list)
traversal(reversed_list)