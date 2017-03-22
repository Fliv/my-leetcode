class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        length = len(nums)
        result = [-1] * length
        for i in range(length - 2, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            stack.append(nums[i])
        for i in range(length - 1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if stack:
                result[i] = stack[-1]
            stack.append(nums[i])
        return result


if __name__ == "__main__":
    solution = Solution()
    print solution.nextGreaterElements([1, 2, 2, 3, 1])
