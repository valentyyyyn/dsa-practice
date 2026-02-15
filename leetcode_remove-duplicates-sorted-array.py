class Solution(object):
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0 # 1. Initialize a pointer for the position of the next unique element.
        for x in nums:
            if i == 0 or x != nums[i - 1]: # 2. Check if the current element is different from the last unique element.
                nums[i] = x # 3. If its unique, place it at the position of the next unique element.
                i += 1 # 4. Move the pointer to the next position for unique elements.
        return i