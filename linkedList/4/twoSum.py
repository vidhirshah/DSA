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
    while pointer != None:
        print(pointer.data)
        pointer = pointer.next
    return

def twoSum(head:Node,value):
    ans = []
    pointer = head
    while pointer != None:
        pointer1 = pointer.next
        while pointer1 != None:
            if pointer1.data + pointer.data == value:
                ans.append([pointer.data,pointer1.data])
            pointer1 = pointer1.next
        pointer = pointer.next
    return ans

array = [1,2,3,4,5]
dll_list = convertToLL(array)
ans = twoSum(dll_list,100)
print(ans)                                                                                                           