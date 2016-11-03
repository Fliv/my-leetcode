# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        p1 = l1
        p2 = l2
        l3 = ListNode(0)
        p3 = l3
        while p1 is not None or p2 is not None:
            if p1 is None:
                p3.next = p2
                break
            elif p2 is None:
                p3.next = p1
                break
            elif p1.val <= p2.val:
                p3.next = p1
                p3 = p3.next
                p1 = p1.next
            else:
                p3.next = p2
                p3 = p3.next
                p2 = p2.next
        return l3.next

if __name__=="__main__":
    def list_to_listnode(nums):
        head = ListNode(0)
        p = head
        for num in nums:
            p.next = ListNode(num)
            p = p.next
        return head.next

    l1 = list_to_listnode([3])
    l2 = list_to_listnode([2, 4, 6, 8, 10])
    solution = Solution()
    l3 = solution.mergeTwoLists(l1, l2)
    p = l3
    while p is not None:
        print p.val
        p = p.next

