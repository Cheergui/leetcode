class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """

        stack = []
        
        for i in range(len(num)):
            while stack and stack[-1]>num[i] and k>0:
                stack.pop()
                k-=1
            stack.append(num[i])
            
        while k>0 and stack:
            stack.pop()
            k-=1
        if len(stack)==0:
            return '0'
        
        if len(stack)==1:
            return str(stack[0])

        if stack[0]=='0':
            while stack and stack[0]=='0':
                stack.pop(0)
            if len(stack)==0:
                return '0'
            return "".join(stack)
        else:
            return "".join(stack)