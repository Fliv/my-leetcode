class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(len(prices) - 1):
            result += max(prices[i + 1] - prices[i], 0)
        return result


if __name__ == "__main__":
    solution = Solution()
    print solution.maxProfit([3, 4, 5])
    print solution.maxProfit([6, 4, 5, 7])
