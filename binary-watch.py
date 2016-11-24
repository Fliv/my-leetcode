class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        li = []
        for n in xrange(1024):
            count = 0
            bitstr = bin(n)[2:]
            while len(bitstr) < 10:
                bitstr = '0' + bitstr
            for bit in bitstr:
                count += int(bit)
            if count == num:
                time_str = self.time(bitstr)
                if time_str:
                    li.append(time_str)
        return li

    def time(self, bitstr):
        m = [32, 16, 8, 4, 2, 1]
        h = [8, 4, 2, 1]
        hours = 0
        mins = 0
        for i, bit in enumerate(bitstr[:4]):
            hours += int(h[i]) * int(bit)
        for i, bit in enumerate(bitstr[4:]):
            mins += int(m[i]) * int(bit)
        if hours > 11:
            return ""
        if mins > 59:
            return ""
        hoursstr = str(hours)
        minstr = str(mins)
        if len(minstr) == 1:
            minstr = '0' + minstr
        return hoursstr + ':' + minstr


if __name__ == "__main__":
    solution = Solution()
    print solution.readBinaryWatch(8)
