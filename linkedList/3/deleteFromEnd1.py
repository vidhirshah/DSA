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

def removeNthFromEnd(head:ListNode,n):
    fast = head
    while n:
        fast = fast.next
        n -= 1
    if fast == None:
        slow = head
        head = head.next
        slow.next = None
        return head
    slow = head
    while fast.next != None:
        fast = fast.next
        slow = slow.next
    temp = slow.next
    slow.next = temp.next
    temp.next = None
    return head

array = [1,2]
linked_list = convertToLL(array)
n = 1
reversed_list = removeNthFromEnd(linked_list,n)
traversal(reversed_list)