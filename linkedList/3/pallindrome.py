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

def isPalindrome(head:ListNode):
    stack = []
    pointer = head
    while pointer != None:
        stack.append(pointer.val)
        pointer = pointer.next
    pointer = head
    while pointer != None and len(stack) > 0:
        if pointer.val != stack.pop():
            return False
        pointer =pointer.next
    return True

array = [1,2,3,4,5,6]
linked_list = convertToLL(array)
reversed_list = isPalindrome(linked_list)
traversal(reversed_list)