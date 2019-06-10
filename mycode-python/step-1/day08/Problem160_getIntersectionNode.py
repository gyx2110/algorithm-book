class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    @classmethod
    def getIntersectionNode(self, headA, headB):
        if(headA == None or headB == None):
            return None
        nodeA = headA
        nodeB = headB
        len_a, len_b = 0, 0
        while nodeA != None or nodeB != None:
            nodeA = nodeA if nodeA == None else nodeA.next
            nodeB = nodeB if nodeB == None else nodeB.next
            len_a = len_a + 1 if nodeA != None else len_a
            len_b = len_b + 1 if nodeB != None else len_b
        gap = abs(len_a-len_b)
        while gap > 0:
            headA = headA if len_a<len_b else headA.next
            headB = headB if len_a>len_b else headB.next
            gap -= 1
        # if len_a > len_b:
        #     while gap != 0:
        #         headA = headA.next
        #         gap -= 1
        # if len_b > len_a:
        #     while gap != 0:
        #         headB = headB.next
        #         gap -= 1
        while headA != headB:
            headA = headA.next
            headB = headB.next
        return headA

    # @classmethod
    # def getIntersectionNode(self, headA, headB):
    #     node = headA
    #     len_a = 0
    #     len_b = 0
    #     while node:
    #         node = node.next
    #         len_a +=1
    #     node = headB
    #     while node:
    #         node = node.next
    #         len_b +=1
    #     gap = abs(len_a-len_b)
    #     if len_a > len_b:
    #         while gap !=0:
    #             headA = headA.next
    #             gap-=1
    #     if len_b > len_a:
    #         while gap !=0:
    #             headB = headB.next
    #             gap-=1
    #     while headA != headB:
    #         headA = headA.next
    #         headB = headB.next
    #     return headA
if __name__ == "__main__":
    list_1 = ListNode(4)
    list_2 = ListNode(1)
    list_3 = ListNode(8)
    list_4 = ListNode(4)
    list_5 = ListNode(5)

    list_1.next = list_2
    list_2.next = list_3
    list_3.next = list_4
    list_4.next = list_4
    list_4.next = list_5


    list_6 = ListNode(5)
    list_7 = ListNode(0)
    list_8 = ListNode(1)

    list_6.next = list_7
    list_7.next = list_8
    list_8.next = list_3

    print Solution.getIntersectionNode(list_1,list_6).val