class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        n, m = x, 0
        while n >= 10:
            m = m * 10 + n % 10
            n /= 10
        return m == x / 10 and n == x % 10

if __name__=='__main__':
    solution = Solution()
    print solution.isPalindrome(-12321)
    print solution.isPalindrome(12324)
    print solution.isPalindrome(42324)
