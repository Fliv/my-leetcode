class NumMatrix(object):

    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        self.sum = []
        self.result = True
        row_len = len(matrix)
        if row_len == 0:
            self.result = False
            return
        col_len = len(matrix[0])
        if col_len == 0:
            self.result = False
            return
        for i in range(row_len+1):
            self.sum.append([])
            for j in range(col_len+1):
                self.sum[i].append(0)
        for i in range(1, row_len+1):
            row_sum = 0
            for j in range(1, col_len+1):
                row_sum += self.matrix[i-1][j-1]
                self.sum[i][j] = self.sum[i-1][j] + row_sum

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.result:
            return 0
        return self.sum[row1][col1] + self.sum[row2+1][col2+1] - self.sum[row1][col2+1] - self.sum[row2+1][col1]



        # Your NumMatrix object will be instantiated and called as such:
        # numMatrix = NumMatrix(matrix)
        # numMatrix.sumRegion(0, 1, 2, 3)
        # numMatrix.sumRegion(1, 2, 3, 4)

if __name__=='__main__':
    numMatrix = NumMatrix([
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
])
    print numMatrix.sumRegion(0, 1, 2, 3)
    print numMatrix.sumRegion(1, 2, 3, 4)
    print numMatrix.sumRegion(2, 1, 4, 3)
    print numMatrix.sumRegion(1, 1, 2, 2)
    print numMatrix.sumRegion(1, 2, 2, 4)