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

def getIntersectionNode(headA:ListNode,headB:ListNode):
    if headA == None or headB == None:
        return None
    pointerA = headA
    pointerB = headB
    while pointerA != pointerB:
        pointerA = pointerA.next
        pointerB = pointerB.next
        if pointerB == pointerA:
            return pointerA
        if pointerA == None:
            pointerA = headB
        if pointerB == None:
            pointerB = headA
    return None

array = [1,2,3]
linked_list = convertToLL(array)
reversed_list = getIntersectionNode(linked_list)
traversal(reversed_list)