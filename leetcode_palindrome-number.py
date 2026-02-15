class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False # 1. Negative numbers never are palindromes.

        original: int = x # 2.1 Save the original number to compare later. 
        reversed_num: int = 0 # 2.2 Initialize a var for the reversed number.

        while x > 0:
            last_digit: int = x % 10 # 3. Extract the last digit of number.
            reversed_num = reversed_num * 10 + last_digit # 4. Put the last digit in the reversed number.
            x = x // 10 # 5. Remove the last digit from the original number.
            
        return reversed_num == original
