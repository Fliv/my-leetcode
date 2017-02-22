class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) < 2:
            return True
        elif word[0].isupper() and word[1].isupper():
            for char in word[2:]:
                if char.islower():
                    return False
            return True
        elif word[0].islower() and word[1].islower():
            for char in word[2:]:
                if char.isupper():
                    return False
            return True
        elif word[0].isupper() and word[1].islower():
            for char in word[2:]:
                if char.isupper():
                    return False
            return True
        else:
            return False

if __name__=="__main__":
    solution = Solution()
    print solution.detectCapitalUse("Google")
    print solution.detectCapitalUse("abcD")
