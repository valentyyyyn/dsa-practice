class Solution:
    def strStr(self, haystack: str, needle: str) -> int: 
        for x in range(len(haystack) - len(needle) + 1): # 1. Iterate through the haystack until the point where the remaining characters are less than the length of the needle.
            if haystack[x:x + len(needle)] == needle: # 2. Check if the substring of haystack starting at index x and having the same length as needle matches needle.
                return x # 3. If it matches, return the current index.
        return -1 # 4. If no match is found, return -1.