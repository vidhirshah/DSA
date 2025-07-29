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

def oddEvenList(head:ListNode):
    if head == None or head.next == None:
        return head
    even_head = head.next
    odd = head
    even = head.next
    while(odd != None and odd.next != None) and (even != None and even.next != None):
        odd.next = odd.next.next
        even.next = even.next.next
        odd = odd.next
        even = even.next
    odd.next = even_head
    return head

array = [1,2,3,4,5]
linked_list = convertToLL(array)
reversed_list = oddEvenList(linked_list)
traversal(reversed_list)