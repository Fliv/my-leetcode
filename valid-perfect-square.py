class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        low = 0
        high = num
        now = num/2
        while high - low > 1:
            square = now ** 2
            if square == num:
                return True
            elif square > num:
                high = now
            else:
                low = now
            now = low + (high - low) / 2
        return False


if __name__=="__main__":
    solution = Solution()
    print solution.isPerfectSquare(121)
