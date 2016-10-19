class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index = dict()
        for i in range(len(nums)):
            index[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in index and index[target - nums[i]] != i:
                return list((i, index[target - nums[i]]))

if __name__=='__main__':
    solution = Solution()
    print solution.twoSum([3, 2, 4], 6)