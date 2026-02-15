class Solution(object):
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix: str = strs[0] # 1. Initialize the prefix to the first str in the list

        for x in strs[1:]: # 2. Iterate from the second str to the end of the list
            while not x.startswith(prefix): # 3. If the current str does not start with the prefix, shorten the prefix by one character
                prefix = prefix[:-1]

                if not prefix:
                    return ""

        return prefix
