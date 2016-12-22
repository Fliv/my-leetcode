class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        z = x ^ y
        count = 0
        while z:
            count += z & 1
            z >>= 1
        return count

if __name__=="__main__":
    solution = Solution()
    print solution.hammingDistance(1, 4)
    print solution.hammingDistance(2**31 - 1, 0)