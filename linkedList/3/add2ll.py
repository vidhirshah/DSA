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

def addTwoNumbers(l1:ListNode,l2:ListNode):
    p1 = l1
    p2 = l2
    carry = 0
    result = ListNode(-1)
    result_pointer = result
    while p1 != None and p2 != None:
        sum = p1.val + p2.val + carry
        carry = int(sum/10)
        result_pointer.next = ListNode(sum%10)
        result_pointer = result_pointer.next
        p1 = p1.next
        p2 = p2.next
    while p1 != None:
        sum = p1.val + carry
        carry = int(sum/10)
        result_pointer.next = ListNode(sum%10)
        result_pointer = result_pointer.next
        p1 = p1.next
    while p2 != None:
        sum = p2.val + carry
        carry = int(sum/10)
        result_pointer.next = ListNode(sum%10)
        result_pointer = result_pointer.next
        p2 = p2.next
    if carry:
        result_pointer.next = ListNode(carry)
        result_pointer = result_pointer.next
    return result.next

array1 = [1,2,3,4,9]
array2 = [1,2,3,4,9]
linked_list1 = convertToLL(array1)
linked_list2 = convertToLL(array2)
addition = addTwoNumbers(linked_list1,linked_list2)
traversal(addition)