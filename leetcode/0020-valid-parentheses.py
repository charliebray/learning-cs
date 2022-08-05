class Solution:
    '''
    Here we just use a stack (represented as a list).

    We pop from the stack if we get a closing bracket, and then compare.
    If they don't match we break early and return False. If we end up with an empty stack
    then the set of parentheses is valid.

    O(n) time complexity.
    '''
    def isValid(self, s: str) -> bool:
        stack_list = []
        a_dict = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in a_dict:
                # If we add a closing bracket to an empty stack, return false
                if len(stack_list) == 0:
                    return False
                # Keep going if open bracket on top of stack matches closing bracket.
                elif stack_list.pop() == a_dict[char]:
                    continue
                # Else, return false
                else:
                    return False
            # If an opening bracket, append to stack
            stack_list.append(char)
        
        # If our stack is empty, then its a valid set of parentheses.
        if len(stack_list) == 0:
            return True
        return False

if __name__ == '__main__':
    solution = Solution()
    s = "())"
    print(solution.isValid(s))