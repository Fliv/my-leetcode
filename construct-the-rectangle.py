class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        width = 0
        i = 1
        while i**2 <= area:
            if area % i == 0:
                width = i
            i += 1
        return [area/width, width]

if __name__ == "__main__":
    solution = Solution()
    print solution.constructRectangle(10000000)
    print solution.constructRectangle(2)
