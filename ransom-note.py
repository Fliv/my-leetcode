import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counter_r = collections.Counter(ransomNote)
        counter_m = collections.Counter(magazine)
        for c in counter_r:
            if counter_r[c] > counter_m[c]:
                return False
        return True

if __name__ == "__main__":
    solution = Solution()
    print solution.canConstruct("a", "aab")
