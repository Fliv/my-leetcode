class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        values = dict()
        for index, num in enumerate(nums):
            values[num] = index
        sorted_nums = sorted(nums, reverse=True)
        nums[values[sorted_nums[0]]] = "Gold Medal"
        if len(nums) < 2:
            return nums
        nums[values[sorted_nums[1]]] = "Silver Medal"
        if len(nums) < 3:
            return nums
        nums[values[sorted_nums[2]]] = "Bronze Medal"
        if len(nums) < 4:
            return nums
        for i in range(3, len(sorted_nums)):
            nums[values[sorted_nums[i]]] = str(i+1)
        return nums

if __name__=="__main__":
    solution = Solution()
    print solution.findRelativeRanks([50, 40, 30, 20, 10])
    print solution.findRelativeRanks([5, 3, 8])
