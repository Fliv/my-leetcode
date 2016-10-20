class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.input = []
        self.output = []
        self.length = 0

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.input.append(x)
        self.length += 1

    def pop(self):
        """
        :rtype: nothing
        """
        self.peek()
        self.output.pop()
        self.length -= 1

    def peek(self):
        """
        :rtype: int
        """
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        head = self.output.pop()
        self.output.append(head)
        return head

    def empty(self):
        """
        :rtype: bool
        """
        return True if self.length == 0 else False

if __name__=='__main__':
    queue = Queue()
    queue.push(1)
    queue.push(3)
    queue.push(5)
    queue.pop()
    queue.pop()
    # queue.pop()
    queue.pop()
    # print queue.peek()
    print queue.empty()