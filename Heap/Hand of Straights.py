class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """
        import heapq
        if len(hand) % groupSize:
            return False
        dic = {}

        for num in hand:
            dic[num] = dic.get(num,0) + 1
        heapq.heapify(hand)
        
        while hand:
            first = heapq.heappop(hand)
            if dic[first] <= 0:
                continue
            for i in range(first,groupSize+first):
                if dic.get(i,0) <= 0:
                    return False
                dic[i] -= 1
        return True