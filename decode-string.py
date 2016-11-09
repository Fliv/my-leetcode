class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        for i, char in enumerate(s):
            if char.isdigit():
                num = self.getNum(s, i)
                j = self.endOfBracket(s, i)
                s1 = s[:i] + num * s[i+len(str(num))+1:j] + s[j+1:]
                return self.decodeString(s1)
        return s

    def endOfBracket(self, s, i):
        index = i
        count = 0
        flag = False
        while index < len(s):
            index += 1
            if s[index] == "[":
                count += 1
                flag = True
            elif s[index] == "]":
                count -= 1
            if count == 0 and flag == True:
                return index

    def getNum(self, s, i):
        index = i
        while index < len(s):
            index += 1
            if not s[index].isdigit():
                break
        return int(s[i:index])

if __name__=="__main__":
    solution = Solution()
    print solution.decodeString("3[a]2[bc]")
    print solution.decodeString("3[a2[c]]")
    print solution.decodeString("100[leetcode]")
