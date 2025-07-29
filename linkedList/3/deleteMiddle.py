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

def deleteMiddle(head:ListNode,n):
    if head == None or head.next == None:
        return None
    fast = head.next.next
    slow = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    temp = slow.next
    slow.next = temp.next
    temp.next = None
    return head

array = [1,2,3]
linked_list = convertToLL(array)
n = 2
reversed_list = deleteMiddle(linked_list,n)
traversal(reversed_list)