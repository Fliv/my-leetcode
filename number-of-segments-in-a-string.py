class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        for i, c in enumerate(s):
            if i == 0 and c != ' ' or s[i-1] == ' ' and c != ' ':
                count += 1
        return count

if __name__=="__main__":
    solution = Solution()
    print solution.countSegments(" Hello, my name   is John    ")
    print solution.countSegments("  123 12")

