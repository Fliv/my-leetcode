class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) is 0:
            return ""
        minStr, minLen = self.minStr(strs)
        for i in range(minLen, -1, -1):
            if self.isMinCommonStr(minStr[0:i], strs):
                return minStr[0:i]
        return ""



    def minStr(self, strs):
        minLen = 2147483647
        minStr = None
        for str in strs:
            if len(str) < minLen:
                minLen = len(str)
                minStr = str
        return minStr, minLen

    def isMinCommonStr(self, minStr, strs):
        for str in strs:
            if not str.startswith(minStr):
                return False
        return True

if __name__=="__main__":
    solution = Solution()
    strs = ['1aab246dcd', '1a246345', '1atd246dg', '1a9764676']
    strs1 = [""]
    print solution.longestCommonPrefix(strs)


