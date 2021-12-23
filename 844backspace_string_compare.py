class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(s):
            stack = []
            for item in s:
                if item != '#':
                    stack.append(item)
                else:
                    if len(stack) > 0:
                        stack.pop()
            return "".join(stack)
        
        return process(s) == process(t)
