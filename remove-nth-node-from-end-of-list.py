# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return None
        p = head
        if self.listCount(head) == n:
            return head.next
        while p is not None:
            if self.isNextRemovable(p, n):
                p.next = p.next.next
                break
            p = p.next
        return head

    def isNextRemovable(self, node, n):
        p = node
        count = 0
        while p.next is not None:
            p = p.next
            count += 1
        if count == n:
            return True
        else:
            return False

    def listCount(self, head):
        p = head
        count = 0
        while p is not None:
            p = p.next
            count += 1
        return count

if __name__=="__main__":
    def list_to_listnode(nums):
        head = ListNode(0)
        p = head
        for num in nums:
            p.next = ListNode(num)
            p = p.next
        return head.next

    l1 = list_to_listnode([1,2,3,4,5])
    solution = Solution()
    l2 = solution.removeNthFromEnd(l1, 1)
    p = l2
    while p is not None:
        print p.val
        p = p.next





