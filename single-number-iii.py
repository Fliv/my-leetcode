class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_sum = 0
        for num in nums:
            xor_sum ^= num
        flag = 1
        while True:
            if flag & xor_sum > 0:
                break
            flag <<= 1
        n, m = 0, 0
        for num in nums:
            if num & flag > 0:
                n ^= num
            else:
                m ^= num
        return [n, m]

if __name__=="__main__":
    solution = Solution()
    print solution.singleNumber([1, -1])
    print 1 ^ -1
