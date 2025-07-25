class ListNode():
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

def convertToLL(array):
    if len(array) == 0:
        return None
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

def getLength(head:ListNode):
    length = 0
    pointer = head
    while pointer != None:
        length += 1
        pointer = pointer.next
    return length

def deleteNode(node:ListNode):
    while node.next.next != None:
        node.val = node.next.val
        node = node.next
    node.val = node.next.val
    node.next = None
    return

array = [1,2,3,4,5]
linked_list = convertToLL(array)
node = linked_list
for i in range(1,3):
    node = node.next
deleteNode(node)
traversal(linked_list)