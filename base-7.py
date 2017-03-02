class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "0"
        base7_str = ""
        base10 = abs(num)
        while base10 > 0:
            base7_str = str(base10 % 7) + base7_str
            base10 /= 7
        if num < 0:
            base7_str = "-" + base7_str
        return base7_str

if __name__ == "__main__":
    solution = Solution()
    print solution.convertToBase7(-100)
    print solution.convertToBase7(14)
