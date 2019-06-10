# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        
        #s0
        if not head or not head.next:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head



        #s1
        # pre,cur = None,head
        # while cur:
        #     pre,pre.next,cur = cur, pre, cur.next
        # return pre
        #s2
        # pre,cur = None,head
        # while cur != None:
        #     next = cur.next
        #     cur.next = pre
        #     pre = cur
        #     cur = next
        # return pre