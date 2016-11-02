class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        MAX = 2147483647
        min_len = MAX
        index = dict()
        for i in range(len(nums)):
            if nums[i] in index and i - index[nums[i]] < min_len:
                min_len = i - index[nums[i]]
            index[nums[i]] = i
        if min_len <= k:
            return True
        else:
            return False

if __name__=="__main__":
    solution = Solution()
    print solution.containsNearbyDuplicate([1,2,3,4,2,5,6,7,4,3], 2)

