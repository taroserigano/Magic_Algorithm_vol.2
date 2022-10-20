class Solution:      # s = "()[]{}"   TS: O(N)
    def isValid(self, s: str) -> bool:

        mapping = {"(": ")", "[": "]",  "{": "}"}
        stack = []
        for c in s:
            if c in mapping:
                stack.append(c)

            elif stack and c == mapping[stack[-1]]:
                stack.pop()
            else:
                return False
        return stack == []    




         


        # 1. if it's open, add it 
        # 2. if closing, check 






class MinStack:

    def __init__(self):
        self.stack = [] 
        self.minstack = [] 

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        
    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] 

        for c in tokens: 
            if c == "+":
                a, b = stack.pop(), stack.pop() 
                stack.append(a + b)

            elif c == "-":
                a, b = stack.pop(), stack.pop() 
                stack.append(b -a)

            elif c =="*":
                a, b = stack.pop(), stack.pop() 
                stack.append(a*b)

            elif c =="/":
                a, b = stack.pop(), stack.pop()     
                stack.append(int(b / a))
            else:
                stack.append(int(c))    

        return stack[0]                    





        
        class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []
        
        def backtrack(open_n, closed_n, path):
            

            if open_n == closed_n == n:
                res.append(path)
                return
            
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] 
        
        for day, temp in enumerate(temperatures):
            
            while stack and stack[-1][1] < temp:    # if larger temp found, add to res 
                stackDay, stackTemp = stack.pop() 
                res[stackDay] = day - stackDay 

            stack.append(( day, temp ))    
        return res     
            
        
        
        # set up res, stack 
        # enumerate temp with day, temp 
        # while stack temp less than stack last temp 
        # pop it
        # deducte days and add to res 
        
        class Solution:     # target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        pair = [[p, s] for p,s in zip(position, speed)]
        stack = []
        for p, s in sorted(pair):
        
            eta = (target-p)/s
            if not stack:
                stack.append(eta)
            else:
                while stack and eta >= stack[-1]:  # this car will exceed it 
                    stack.pop()                    # leave only "faster" cars 

                stack.append(eta)
        return len(stack)


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack, mx = [], 0 
        heights += [0]

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]

                if not stack:
                    width = i
                else:
                    width = i - (stack[-1]+1)

                mx = max(mx, height*width)
            stack.append(i)         

        return mx        


# 1. Add [0] on right, this will check ALL because stack[-1] > "0"
# 2. whenever the new height is LESS, then output the max at this point by
#  height and width = i - (stack[-1]+1) 
#  +1 BECAUSE stack has been Popped 




            if open_n < n:
                backtrack(open_n + 1, closed_n, path + "(")
             

            if closed_n < open_n:
                backtrack(open_n, closed_n + 1, path + ")")
                
        backtrack(0, 0, "")
        return res  





