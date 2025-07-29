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
    temp = head
    values = []
    while temp != None and temp.next != None:
        values.append(temp.val)
        temp = temp.next.next
    if temp != None:
        values.append(temp.val)
    temp = head.next
    while temp != None and temp.next != None:
        values.append(temp.val)
        temp = temp.next.next
    if temp != None:
        values.append(temp.val)
    temp = head
    for i in values:
        temp.val = i
        temp = temp.next
    print(values)
    return head

array = [1,2,3,4,5,6]
linked_list = convertToLL(array)
reversed_list = oddEvenList(linked_list)
traversal(reversed_list)