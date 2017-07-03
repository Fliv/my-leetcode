class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        # sum1 = 2000
        # com = []
        # i = 0
        # while i < sum1 + 1 and i < len(list1):
        #     j = 0
        #     while j < sum1 + 1 and j < len(list2):
        #         if list1[i] == list2[j] and i + j == sum1:
        #             com.append(list1[i])
        #         if list1[i] == list2[j] and i + j < sum1:
        #             com = []
        #             com.append(list1[i])
        #             sum1 = i+j
        #         j += 1
        #     i += 1
        # return com
        sum0 = 2000
        com = []
        map1 = {u: i for i, u in enumerate(list1)}
        for j, v in enumerate(list2):
            k = map1.get(v, 1e9)
            if k + j < sum0:
                sum0 = k + j
                com = [v]
            elif k + j == sum0:
                com.append(v)
        return com

if __name__ == "__main__":
    solution = Solution()
    print solution.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])
    print solution.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], 
["Tapioca Express", "Shogun", "Burger King"])
