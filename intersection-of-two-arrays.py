class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        inter = []
        sorted_nums1 = sorted(nums1)
        sorted_nums2 = sorted(nums2)
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if sorted_nums1[i] == sorted_nums2[j]:
                if not inter or inter[-1] != sorted_nums1[i]:
                    inter.append(sorted_nums1[i])
                i += 1
                j += 1
            elif sorted_nums1[i] < sorted_nums2[j]:
                i += 1
            else:
                j += 1
        return inter

if __name__ == "__main__":
    solution = Solution()
    print solution.intersection([1, 2, 2, 1], [2, 2])
    print solution.intersection([2, 2, 2, 2, 2], [2, 2])

