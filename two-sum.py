class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for i in range(length - 1):
            for j in range(i+1, length):
                if nums[i]+nums[j] == target:
                    return list((i, j))

if __name__=='__main__':
    solution = Solution()
    print solution.twoSum([2, 7, 11, 15], 9)
