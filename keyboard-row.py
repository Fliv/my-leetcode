class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        # alp_table = {}
        # row1 = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P']
        # row2 = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L']
        # row3 = ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        # for alp in row1:
        #     alp_table[alp] = 1
        # for alp in row2:
        #     alp_table[alp] = 2
        # for alp in row3:
        #     alp_table[alp] = 3
        # print alp_table

        alp_table = {'A': 2, 'C': 3, 'B': 3, 'E': 1, 'D': 2, 'G': 2, 'F': 2, 'I': 1, 'H': 2,
                     'K': 2, 'J': 2, 'M': 3, 'L': 2, 'N': 3, 'Q': 1, 'P': 1, 'S': 2, 'R': 1,
                     'U': 1, 'T': 1, 'W': 1, 'V': 3, 'Y': 1, 'X': 3, 'Z': 3, 'O': 1}
        same_line_words = []
        for word in words:
            if not word:
                continue
            same_line_flag = True
            for alp in word.upper():
                if alp_table[alp] != alp_table[(word.upper())[0]]:
                    same_line_flag = False
                    break
            if same_line_flag:
                same_line_words.append(word)
        return same_line_words


if __name__ == "__main__":
    solution = Solution()
    print solution.findWords(["asdfghjkl", "qwertyuiop", "zxcvbnm"])
