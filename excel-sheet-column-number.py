class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        count = 1
        for c in s[::-1]:
            num += (ord(c) - ord('A') + 1) * count
            count *= 26
        return num

if __name__ == "__main__":
    solution = Solution()
    print solution.titleToNumber("AB")
    print solution.titleToNumber("A")
    print solution.titleToNumber("")

