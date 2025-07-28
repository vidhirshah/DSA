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

def middleNode(head:ListNode):
    pointer1 = head
    pointer2 = head
    while pointer2 != None:
        if pointer2.next == None:
            return pointer1
        pointer1 = pointer1.next
        pointer2 = pointer2.next.next
    return pointer1

array = [1,2,3,4,5,6]
linked_list = convertToLL(array)
middle = middleNode(linked_list)
traversal(middle)