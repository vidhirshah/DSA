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

def merge(left_Head:ListNode,right_head:ListNode):
    dummyNode = ListNode(-1)
    pointer = dummyNode
    while left_Head != None and right_head != None:
        if left_Head.val <= right_head.val:
            pointer.next = left_Head
            left_Head = left_Head.next
        else:
            pointer.next = right_head
            right_head = right_head.next
        pointer = pointer.next
    if left_Head != None:
        pointer.next = left_Head
    if right_head != None:
        pointer.next = right_head
    return dummyNode.next

def sortLl(head:ListNode):
    if head == None or head.next == None:
        return head
    fast = head.next
    slow = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    right_head = slow.next
    left_head = head
    slow.next = None
    left_head = sortLl(left_head)
    right_head = sortLl(right_head)
    return merge(left_head,right_head)

array = [1,2,4,6,7,3,6,0,3]
linked_list = convertToLL(array)
reversed_list = sortLl(linked_list)
traversal(reversed_list)