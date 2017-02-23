class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = 0
        tmp = 0
        for num in nums:
            if num == 0:
                if tmp > max_num:
                    max_num = tmp
                tmp = 0
            else:
                tmp += 1
        return max_num if max_num > tmp else tmp

if __name__ == "__main__":
    solution = Solution()
    print solution.findMaxConsecutiveOnes([1,0,1,1,1,1])
    print solution.findMaxConsecutiveOnes([0,0,0,0,0])
