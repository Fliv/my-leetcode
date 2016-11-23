class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        num_list = []
        fizz = 0
        buzz = 0
        for num in range(1, n+1):
            fizz += 1
            buzz += 1
            if buzz == 5 and fizz == 3:
                fizz = 0
                buzz = 0
                num_list.append("FizzBuzz")
            elif fizz == 3:
                fizz = 0
                num_list.append("Fizz")
            elif buzz == 5:
                buzz = 0
                num_list.append("Buzz")
            else:
                num_list.append(str(num))
        return num_list

if __name__=="__main__":
    solution = Solution()
    print solution.fizzBuzz(1)
