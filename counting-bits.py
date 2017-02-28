class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        nums = [0]
        for i in range(1, num+1):
            nums.append(nums[i >> 1] + i % 2)
        return nums


if __name__ == "__main__":
    solution = Solution()
    print solution.countBits(10)
