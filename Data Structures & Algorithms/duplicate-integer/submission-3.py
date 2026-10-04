class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        bag=set()
        for x in nums:
            if x in bag:
                return True
            bag.add(x)
        return False
            
   
    
        