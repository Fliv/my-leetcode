class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bit = 1
        nums = []
        copy = num
        while copy > 0:
            nums.append(copy & bit)
            copy >>= 1
        rev = 0
        for j in nums[::-1]:
            rev = (rev << 1) + (j ^ 1)
        return rev

if __name__ == "__main__":
    solution = Solution()
    print solution.findComplement(20)
