class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        if r == l + 1:
            return [l + 1, r + 1]
        while l < r:
            suma = numbers[l] + numbers[r] 
            if suma == target:
                break
            elif suma > target:
                r -= 1
            else:
                l += 1
        return [l + 1, r + 1]