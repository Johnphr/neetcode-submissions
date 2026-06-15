class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        top_nums = []
        for i in range(k):
            top_nums.append(max(count, key=count.get))
            count.pop(max(count, key=count.get))
        return top_nums
        
        