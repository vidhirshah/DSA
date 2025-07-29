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
    temp = []
    pointer = head
    while pointer != None:
        temp.append(pointer.val)
        pointer = pointer.next
    temp.sort()
    pointer = head
    while len(temp) > 0 and pointer != None:
        pointer.val = temp.pop(0)
        pointer = pointer.next
    return head

array = [1,2,3]
linked_list = convertToLL(array)
reversed_list = sortLl(linked_list)
traversal(reversed_list)