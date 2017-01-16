class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n < 2:
        #     return 1
        # else:
        #     return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        count1 = 2
        count2 = 1
        count = 0
        for i in range(3, n+1):
            count = count1 + count2
            count2 = count1
            count1 = count
        return count


if __name__=="__main__":
    solution = Solution()
    print solution.climbStairs(3)
    print solution.climbStairs(2)
    print solution.climbStairs(35)
    print solution.climbStairs(100)

