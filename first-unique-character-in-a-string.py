class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return -1
        hashset = dict()
        for char in s:
            if char in hashset:
                hashset[char] += 1
            else:
                hashset[char] = 1
        for index, char in enumerate(s):
            if hashset[char] == 1:
                return index
        return -1

if __name__ == "__main__":
    solution = Solution()
    print solution.firstUniqChar("leetcode")
    print solution.firstUniqChar("loveleetcode")
