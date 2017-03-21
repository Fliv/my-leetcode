class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums_len = len(nums)
        result = [1] * nums_len
        left = 1
        right = 1
        for i in range(1, nums_len):
            left *= nums[i - 1]
            result[i] *= left
            right *= nums[nums_len - i]
            result[nums_len - i - 1] *= right
        return result


if __name__ == "__main__":
    solution = Solution()
    print solution.productExceptSelf([1, 2, 3, 4])
    print solution.productExceptSelf([2])
