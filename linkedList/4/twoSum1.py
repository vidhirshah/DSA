class Node():
    def __init__(self,data,next=None,back =None):
        self.data = data
        self.next = next
        self.back = back

def convertToLL(array):
    head = Node(array[0])
    pointer = head
    for i in range(1,len(array)):
        temp = Node(array[i],None,pointer)
        pointer.next = temp
        pointer = pointer.next
    return head

def traversal(head:Node):
    pointer = head
    while pointer.next != None:
        pointer = pointer.next
    tail = pointer
    while tail != None:
        print(tail.data)
        tail = tail.back
    return

def twoSum(head:Node,value):
    ans = []
    pointer = head
    while pointer.next != None:
        pointer = pointer.next
    tail = pointer
    while  head != tail and head.back != tail:
        if tail.data + head.data == value:
            ans.append([head.data,tail.data])
            head = head.next
            tail = tail.back
        elif tail.data + head.data < value:
            head = head.next
        else:
            tail = tail.back
    return ans

array = [1,2,3,4,5]
dll_list = convertToLL(array)
ans = twoSum(dll_list,9)
print(ans)