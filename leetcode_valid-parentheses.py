class Solution(object):
    def isValid(self, s: list[str]) -> bool:
        stack: list[str] = [] # 1. Initialize an empty stack to keep track of opening parentheses. 

        pair: dict[str, str] = {
            ")": "(", 
            "]": "[", 
            "}": "{"
        } # 2. Create a dictionary to map closing parentheses to their corresponding opening parentheses.

        for char in s:
            if char in pair.values():  
                stack.append(char) # 3. If the character is an opening parenthesis, push it onto the stack.
            elif char in pair:  
                if not stack or stack[-1] != pair[char]: # 4. If the character is a closing parenthesis, check if the stack is empty or if the top of the stack does not match the corresponding opening parenthesis. If either condition is true, return False.
                    return False
                stack.pop() # 5. If the top of the stack matches the corresponding opening parenthesis, pop it from the stack.
 
        return not stack # 6. After processing all characters, if the stack is empty, return True; otherwise, return False.
