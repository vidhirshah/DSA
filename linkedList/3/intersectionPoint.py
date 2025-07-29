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

def sortLl(headA:ListNode,headB:ListNode):
    hash = []
    pointer = headA
    while pointer != None:
        hash.append(pointer)
        pointer = pointer.next
    pointer = headB
    while pointer != None:
        if pointer in hash:
            return pointer
        pointer = pointer.next
    return None

array = [1,2,3]
linked_list = convertToLL(array)
reversed_list = sortLl(linked_list)
traversal(reversed_list)