# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        counter = head
        result = ListNode()
        total = 0
        while counter.next != None:
            total += 1
           
            counter = counter.next
        if(total == 0):
            return head
        if((total % 2) == 0):
            middle = round(total/2) + 1
            
        else:
            middle = ((total/2) + (total%2))
            print((total%2))
        print('middle', middle)
        
        
        total = 1
        while head.val != None:
            if(total >= middle):
                return head
            total += 1  
            head = head.next