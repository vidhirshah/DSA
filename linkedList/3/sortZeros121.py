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

def sortLl(head:ListNode):
    if head == None or head.next == None:
        return None
    zero_head = ListNode(-1)
    zero = zero_head
    one_head = ListNode(-1)
    one = one_head
    two_head = ListNode(-1)
    two = two_head
    pointer = head
    while pointer != None:
        if pointer.val == 0:
            zero.next = pointer
            zero = zero.next
        elif pointer.val == 1:
            one.next = pointer
            one = one.next
        else:
            two.next = pointer
            two = two.next
        pointer = pointer.next
    if one_head.next != None:
        zero.next = one_head.next
        one.next = two_head.next
    else:
        zero.next = two_head.next
    two.next = None
    return zero_head.next

array = [2,0,2]
linked_list = convertToLL(array)
reversed_list = sortLl(linked_list)
traversal(reversed_list)