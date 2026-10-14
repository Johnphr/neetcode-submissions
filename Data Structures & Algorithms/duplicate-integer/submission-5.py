class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mySet = set() # Initialize set
        for n in nums:
            if n in mySet:
                return True # If the number is in the set, it repeats, so True
            mySet.add(n) # If not, we add the number to the set
        return False