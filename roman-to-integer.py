class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        strTable = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        romanSum = 0
        for i in range(len(s)):
            if i == len(s) - 1:
                romanSum += strTable[s[i]]
            else:
                if strTable[s[i]] < strTable[s[i+1]]:
                    romanSum -= strTable[s[i]]
                else:
                    romanSum += strTable[s[i]]
        return romanSum

if __name__=='__main__':
    solution = Solution()
    print solution.romanToInt('MCMXC')