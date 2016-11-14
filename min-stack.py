class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.index = -1
        self.min_index = -1


    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_index == -1:
            self.min_index = len(self.stack) - 1
        elif self.top() < self.stack[self.min_index]:
            self.min_index = len(self.stack) - 1

    def pop(self):
        """
        :rtype: void
        """
        self.stack.pop()
        if not self.stack:
            self.min_index = -1
        elif self.min_index == len(self.stack):
            self.min_index = 0
            for i, num in enumerate(self.stack):
                if num < self.stack[self.min_index]:
                    self.min_index = i

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            return None
        return self.stack[self.min_index]




        # Your MinStack object will be instantiated and called as such:
if __name__=="__main__":
    obj = MinStack()
    obj.push(1)
    obj.push(2)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print param_3
    print param_4