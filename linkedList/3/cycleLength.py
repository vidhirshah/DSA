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

def hasCycle(head:ListNode):
    if head == None or head.next == None:
        return False
    hash = {}
    timer = 0
    pointer = head
    while pointer != None:
        if pointer in hash:
            return timer - hash[pointer]
        hash[pointer] = timer + hash.get(pointer,0)
        
        pointer = pointer.next
    return 0

array = [1,2,3,4,5,6]
linked_list = convertToLL(array)
reversed_list = hasCycle(linked_list)
traversal(reversed_list)