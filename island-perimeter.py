class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        count = 0
        for i, x in enumerate(grid):
            for j, y in enumerate(x):
                if y == 1:
                    count += self.get_len(i, j, grid)
        return count

    def get_len(self, i, j, grid):
        length = 0
        if i == 0 or i > 0 and grid[i - 1][j] == 0:
            length += 1
        if j == 0 or j > 0 and grid[i][j - 1] == 0:
            length += 1
        if i == len(grid) - 1 or i < len(grid) - 1 and grid[i + 1][j] == 0:
            length += 1
        if j == len(grid[0]) - 1 or j < len(grid[0]) - 1 and grid[i][j + 1] == 0:
            length += 1
        return length


if __name__ == "__main__":
    solution = Solution()
    island = [[0, 1, 0, 0],
              [1, 1, 1, 0],
              [0, 1, 0, 0],
              [1, 1, 0, 0]]
    print solution.islandPerimeter(island)
