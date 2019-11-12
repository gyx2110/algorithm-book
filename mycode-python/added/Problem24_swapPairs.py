class Solution(object):
    def swapPairs(self, head):
        if head==None or head.next==None:
            return head
        next = head.next
        head.next = self.swapPairs(next.next)
        next.next = head
        return next