class Node():
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

def convertToLL(array):
    head = Node(array[0])
    pointer = head
    for i in range(1,len(array)):
        temp = Node(array[i])
        pointer.next = temp
        pointer = pointer.next
    return head

array = [1,2,3,4,5]
linked_list = convertToLL(array)
print(linked_list.data)