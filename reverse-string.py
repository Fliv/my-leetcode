class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        s1 = []
        s2 = []
        for char in s:
            s1.append(char)
        length = len(s)
        while length:
            s2.append(s1[length - 1])
            length -= 1
        return "".join(s2)

if __name__=="__main__":
    solution = Solution()
    print solution.reverseString("abcdefg")
    print solution.reverseString("")