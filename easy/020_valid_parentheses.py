class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {
            "(":")",
            "[":"]",
            "{":"}",
        }
        
        for chr in s:
            if chr in dic.keys():
                stack.append(chr)
            elif chr in dic.values():
                if len(stack) == 0:
                    return False
                last = stack.pop(-1)
                if dic[last] != chr:
                    return False
                
        return not stack
