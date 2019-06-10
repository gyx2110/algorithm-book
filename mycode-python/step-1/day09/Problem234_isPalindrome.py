class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution(object):
    def isPalindrome(self, head):
        if head == None or head.next == None:
            return True
        fast = head
        mid = head.next
        stack = []
        while mid:
            if fast.next and fast.next.next:
                mid = mid.next
                fast = fast.next.next
            else:
                stack.append(mid.val)
                mid = mid.next        
        while len(stack)!=0:
            if stack.pop() != head.val:
                return False
            head = head.next
        return True
if __name__ == "__main__":
    l1 = ListNode(1)
    l2 = ListNode(0)
    l3 = ListNode(1)
    l4 = ListNode(1)
    l1.next = l2
    l2.next = l3
    #l3.next = l4
    print Solution.isPalindrome(l1)