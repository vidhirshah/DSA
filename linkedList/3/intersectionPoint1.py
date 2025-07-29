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
    nA = 0
    pointerA = headA
    while pointerA != None:
        pointerA = pointerA.next
        nA += 1
    nB = 0
    pointerB = headB
    while pointerB != None:
        pointerB = pointerB.next
        nB += 1
    pointerA = headA
    pointerB = headB
    if nA > nB:
        while nA != nB:
            pointerA = pointerA.next
            nA -= 1
    else:
        while nA != nB:
            pointerB = pointerB.next
            nB -= 1
    while pointerA != None and pointerB != None:
        if pointerA == pointerB :
            return pointerA
        pointerA = pointerA.next
        pointerB = pointerB.next
    return None

array = [1,2,3]
linked_list = convertToLL(array)
reversed_list = getIntersectionNode(linked_list)
traversal(reversed_list)