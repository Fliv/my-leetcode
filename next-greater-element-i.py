class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        next_greater_nums = []
        for target_num in findNums:
            flag = False
            for num in nums[nums.index(target_num):]:
                if num > target_num:
                    next_greater_nums.append(num)
                    flag = True
                    break
            if not flag:
                next_greater_nums.append(-1)
        return next_greater_nums

if __name__=="__main__":
    solution = Solution()
    print solution.nextGreaterElement([2,4], [1,2,3,4])
    print solution.nextGreaterElement([4,1,2], [1,3,4,2])