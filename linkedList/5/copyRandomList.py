class Node():
    def __init__(self,val=0,next=None,random = None):
        self.val = val
        self.next = next
        self.random = random

def traversal(head :Node):
    pointer = head
    while pointer != None:
        print(pointer.val)
        pointer = pointer.next
    return

def copyRandomList(head:Node):
    hash = {}
    pointer = head
    newhead = Node(-1,None,None)
    newpointer = newhead
    while pointer != None:
        newpointer.next = Node(pointer.val,None,None)
        newpointer = newpointer.next
        hash[pointer] = [pointer.random,newpointer]
        pointer = pointer.next
    for i in hash.keys():
        if hash[i][0] != None:
            newNode = hash[i][0]
            newNode = hash[newNode][1]
            hash[i][1].random = newNode
    return newhead.next

node0 = Node(7,None,None)
node1 = Node(13,None,None)
node2 = Node(11,None,None)
node3 = Node(10,None,None)
node4 = Node(1,None,None)
linked_list = node0
node0.next = node1
node1.random = node0
node1.next = node2
node2.random = node4
node2.next = node3
node3.random = node2
node3.next = node4
node4.random = node0
linked_list = copyRandomList(linked_list)
traversal(linked_list)