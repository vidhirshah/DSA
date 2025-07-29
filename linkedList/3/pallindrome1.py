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
    current = head
    prev = None
    while current != None:
        front = current.next
        current.next = prev
        prev = current
        current = front
    return prev

def isPalindrome(head:ListNode):
    if head == None or head.next == None:
        return True
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        fast = fast.next.next
        slow = slow.next
    if fast.next == None:
        reversed_list = reverseList(slow)
    else:
        reversed_list = reverseList(slow.next)
    left = head
    right = reversed_list
    while right != None:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True


array = [1,2,3,4,5,6]
linked_list = convertToLL(array)
reversed_list = reverseList(linked_list)
traversal(reversed_list)