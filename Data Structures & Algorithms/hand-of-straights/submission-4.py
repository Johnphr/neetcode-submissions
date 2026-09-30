class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        limit = max(hand)
        myMap = [0] * (limit + 1)
        # print(myMap[0:10])
        for num in hand:
            myMap[num] += 1
        for i in range(len(myMap)):
            if myMap[i] == -1:
                # print('hee', i, myMap)
                return False
            if myMap[i] == 0:
                continue
            if i + groupSize > limit + 1:
                # print('here', i)
                # print(i)
                return False
            while myMap[i] > 0:
            # print(i, i + groupSize)
                for j in range(i, i + groupSize):
                    myMap[j] -= 1
            # print(myMap[0:10])
        return True
