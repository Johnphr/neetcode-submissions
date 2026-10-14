import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Group the numbers by frequency
        myMap = {}
        for n in nums:
            myMap[n] = myMap.get(n, 0) + 1

        # 2. Store the frequencies as a list of tuples
        myList = []
        for n, f in myMap.items():
            myList.append((-f, n))

        # 3. Heapify the list of tuples
        heapq.heapify(myList)

        # 4. Add the top k elements to the result and return
        res = []
        for i in range(k):
            res.append(myList[0][1])
            heapq.heappop(myList)
        return res