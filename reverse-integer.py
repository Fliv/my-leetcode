class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 1
        abs_x = x
        nums = []
        result = 0
        if x > 2147483647 or x < -2147483648:
            return 0
        if x < 0:
            flag = -1
            abs_x = -x

        while abs_x:
            nums.append(abs_x % 10)
            abs_x /= 10
        for i in range(len(nums)):
            result *= 10
            result += nums[i]
            if result > 214748364 and i < 9 and len(nums) == 10:
                return 0
        return result * flag

if __name__=='__main__':
    solution = Solution()
    print solution.reverse(563847412)
