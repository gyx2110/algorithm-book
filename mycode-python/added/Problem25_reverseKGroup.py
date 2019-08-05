class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    stack = []
    def resign(self,pre,next):
        node = self.stack.pop()
        if pre:
            pre.next = node
        while self.stack:
            p = self.stack.pop()
            node.next = p
            node = node.next
        node.next = next
        return node

    def reverseKGroup(self, head, k):
        cur = head
        pre,new_head = None,None
        while cur:
            next = cur.next
            self.stack.append(cur)
            if len(self.stack)==k:
                pre = self.resign(pre,next)
                new_head = new_head if new_head else cur
            cur = next
        del self.stack[:] #必须要清空，不然会影响后续的case
        return new_head if new_head else head
        
if __name__ == "__main__":
    s = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    res = s.reverseKGroup(a,3)
    while res:
        print res.val
        res = res.next
    s = Solution()
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    res = s.reverseKGroup(a,3)
    while res:
        print res.val
        res = res.next