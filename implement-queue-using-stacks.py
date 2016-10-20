class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue = []
        self.sp = -1

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue.append(x)
        self.sp += 1

    def pop(self):
        """
        :rtype: nothing
        """
        self.queue.pop(0)
        self.sp -= 1

    def peek(self):
        """
        :rtype: int
        """
        return self.queue[0]

    def empty(self):
        """
        :rtype: bool
        """
        return True if self.sp == -1 else False

if __name__=='__main__':
    queue = Queue()
    queue.push(1)
    queue.push(3)
    queue.pop()
    # queue.pop()
    print queue.peek()
    print queue.empty()