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
    count0 = 0
    count1 = 0
    count2 = 0
    pointer = head
    while pointer != None:
        if pointer.val == 0:
            count0 += 1
        elif pointer.val == 1:
            count1 += 1
        else:
            count2 += 1
        pointer = pointer.next
    pointer = head
    while count0 != 0:
        pointer.val = 0
        count0 -= 1
        pointer = pointer.next
    while count1 != 0:
        pointer.val = 1
        count1 -= 1
        pointer = pointer.next
    while count2 != 0:
        pointer.val = 2
        count2 -= 1
        pointer = pointer.next
    return head

array = [0,1,2,1,2,0]
linked_list = convertToLL(array)
reversed_list = sortLl(linked_list)
traversal(reversed_list)