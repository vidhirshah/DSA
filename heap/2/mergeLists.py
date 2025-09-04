class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
def insert(head:ListNode,val):
    pointer = head
    while pointer.next != None:
        pointer = pointer.next
    pointer.next = ListNode(val)
    return head

def traversal(head:ListNode):
    pointer = head
    while pointer != None:
        print(pointer.val)
        pointer = pointer.next
    return

def mergeKLists(lists: list[ListNode]) -> ListNode:
    if not lists or len(lists) == 0:
        return None
    def merge(l1:ListNode,l2:ListNode):
        ans = ListNode(-1)
        p1 = l1
        p2 = l2
        p3 = ans
        while p1 != None and p2 != None:
            if p1.val <= p2.val:
                p3.next = p1
                p3 = p3.next
                p1 = p1.next
            else:
                p3.next = p2
                p3 = p3.next
                p2 = p2.next
        while p1 != None:
            p3.next = p1
            p3 = p3.next
            p1 = p1.next
        while p2 != None:
            p3.next = p2
            p3 = p3.next
            p2 = p2.next
        return ans.next        
    
    while len(lists) > 1:
        temp = []
        for i in range(0,len(lists),2):   
            l1 = lists[i]
            if i + 1 < len(lists):
                l2 = lists[i+1]
                temp.append(merge(l1,l2))
            else:
                temp.append(l1)
        lists = temp
    return lists[0]
    
inp = [[1,4,5],[1,3,4],[2,6]]
lists = []
for i in inp:
    head = ListNode(i[0])
    for j in i[1:]:
        head = insert(head,j)
    lists.append(head)

traversal(mergeKLists(lists))