# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node_dict = {}
        phead = ListNode(0)
        phead.next = head
        p = phead
        while p.next is not None:
            if p.next.val in node_dict:
                p.next = p.next.next
            else:
                node_dict[p.next.val] = True
                p = p.next
        return phead.next

if __name__ == "__main__":
    def list_to_listnode(nums):
        head = ListNode(0)
        p = head
        for num in nums:
            p.next = ListNode(num)
            p = p.next
        return head.next
    l1 = list_to_listnode([1,1,1,2,33,4,4,5,5,5,6,5,4])
    l1 = list_to_listnode([1])
    solution = Solution()
    l2 = solution.deleteDuplicates(l1)
    p = l2
    while p:
        print p.val
        p = p.next

