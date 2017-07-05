class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops:
            return m*n
        x, y = 1e9, 1e9
        for op in ops:
            if op[0] < x:
                x = op[0]
            if op[1] < y:
                y = op[1]
        return x*y

if __name__ == "__main__":
    solution = Solution()
    print solution.maxCount(3, 3, [[2,2],[3,3]])
    print solution.maxCount(3, 3, [])

