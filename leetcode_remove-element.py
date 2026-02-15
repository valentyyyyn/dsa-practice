class Solution:
    def removeElement(self, nums: list[int], val: int) -> int: 
        different_numbers: int = 0 # 1. Var to track numbers different from val. 
                
        for x in nums: 
            if x != val: 
                nums[different_numbers] = x # 2. If the number is different from val, place it at the index indicated by different_numbers.
                different_numbers += 1 # 3. Update different_numbers for the index and final count.
        
        return different_numbers