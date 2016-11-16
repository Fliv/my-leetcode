# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        phead = ListNode(0)
        phead.next = head
        p = phead
        p1 = ListNode(0)
        p2 = ListNode(0)
        while p.next:
            if not p.next.next:
                break
            p1.next = p.next
            p2.next = p.next.next
            p1.next.next = p2.next.next
            p2.next.next = p1.next
            p.next = p2.next
            p = p.next.next
        return phead.next

if __name__ == "__main__":
    def list_to_listnode(nums):
        head = ListNode(0)
        p = head
        for num in nums:
            p.next = ListNode(num)
            p = p.next
        return head.next

    l1 = list_to_listnode([1, 2, 3, 4, 5])
    solution = Solution()
    l2 = solution.swapPairs(l1)
    p0 = l2
    while p0 is not None:
        print p0.val
        p0 = p0.next
