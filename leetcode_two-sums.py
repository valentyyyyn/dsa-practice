class Solution(object):
    def twoSum(self, nums: list[int], target: int):
        seen: dict[int, int] = {} # 1. Initialize a empty dictionary for save the seen numbers and their indexes. 

        for index, num in enumerate(nums): # 2. Iterate through the numbers and their indexes. 
            complement: int = target - num # 3. Calculate the complement of the current number by subtracting it from the target.

            if complement in seen:
                return [seen[complement], index] # 4. If the complement is in the seen dictionary, return the indexes of the complement and the current number.

            seen[num] = index # 5. If the complement is not in the seen dictionary, add the current number and its index to the seen dictionary.