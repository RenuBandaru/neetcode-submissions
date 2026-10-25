from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq = Counter(nums)
        duplicate = False

        for value in freq.values():
            if value > 1: 
                duplicate = True
        
        return duplicate
    
        