# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        add = 1 if l1.val + l2.val >= 10 else 0
        l3 = ListNode((l1.val + l2.val) % 10)
        p1 = l1
        p2 = l2
        p3 = l3
        while p1.next and p2.next:
            p1 = p1.next
            p2 = p2.next
            next_val = p1.val + p2.val + add
            add = 0
            if next_val >= 10:
                next_val -= 10
                add = 1
            p3.next = ListNode(next_val)
            p3 = p3.next
        while p1.next:
            p1 = p1.next
            next_val = add + p1.val
            add = 0
            if next_val >= 10:
                next_val -= 10
                add = 1
            p3.next = ListNode(next_val)
            p3 = p3.next
        while p2.next:
            p2 = p2.next
            next_val = add + p2.val
            add = 0
            if next_val >= 10:
                next_val -= 10
                add = 1
            p3.next = ListNode(next_val)
            p3 = p3.next
        if add > 0:
            p3.next = ListNode(add)
        return l3


def int_to_list(x):
    list_node = ListNode(x % 10)
    p = list_node
    x /= 10
    while x > 0:
        mod = x % 10
        x /= 10
        p.next = ListNode(mod)
        p = p.next
    return list_node


if __name__=='__main__':
    l1 = int_to_list(789)
    l2 = int_to_list(456)
    solution = Solution()
    l3 = solution.addTwoNumbers(l1, l2)

    p = l3
    while p:
        print p.val
        p = p.next