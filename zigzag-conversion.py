class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        matrix = []
        for i in range(numRows):
            matrix.append('')
        for i in range(len(s)):
            mod = i % ((numRows - 1) * 2)
            index = mod if mod < numRows else 2 * (numRows - 1) - mod
            matrix[index] += s[i]
        return ''.join(matrix)

if __name__=='__main__':
    solution = Solution()
    print solution.convert("PAYPALISHIRING", 3)
