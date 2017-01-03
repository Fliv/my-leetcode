class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        m = min(nums)
        count = 0
        for i in nums:
            count += (i - m)
        return count

if __name__=="__main__":
    solution = Solution()
    print solution.minMoves([1, 2, 3])
    print solution.minMoves([1])
