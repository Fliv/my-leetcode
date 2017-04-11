class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i = 0
        j = len(numbers) - 1
        while numbers[i] + numbers[j] != target and i < j:
            if numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1
        return [i+1, j+1]

if __name__ == "__main__":
    solution = Solution()
    print solution.twoSum([2, 7, 11, 15], 9)