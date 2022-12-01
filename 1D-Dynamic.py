



class Solution:
    def climbStairs(self, n: int) -> int:

        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2,n+1):
                dp[i] = dp[i-1]+dp[i-2]
        return dp[n]

        class Solution:    # cost = [10,*15,20]  *start - coin result= [10, 15, 30, 40, 60]
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        for i in range(2, len(cost)): 

            cost[i] +=  min(cost[i-1], cost[i-2])
        print(cost)
        return min(cost[-1], cost[-2])   # [10, 15, 30, 40, 60]
      
      
      class Solution: # nums = [2,7,9,3,1]
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 2: return max(nums)
        
        sums = [0] * len(nums)
        sums[0] = nums[0]
        sums[1]= max(nums[0], nums[1])
        
        for i in range(2, len(nums)):

            sums[i] = max(sums[i-2] + nums[i], sums[i-1])

        return sums[-1]    # [2, 7, 11, 11, 12]
        
        
        
        class Solution: # nums = [2,3,2]
    def rob(self, nums: List[int]) -> int:
        
        def helper(nums): 

            sums = [0] * len(nums) 
            sums[0] = nums[0] 
            sums[1] = max(nums[0], nums[1]) 

            for i in range(2, len(nums)): 
                sums[i] = max(nums[i] + sums[i-2], sums[i-1]) 

            return max(sums[-1], sums[-2]) 

        if len(nums) <= 2: return max(nums) 

        return max(helper(nums[1:]), helper(nums[:-1]))      

      class Solution:     # s = "babad" Output: "bab"  T: O(n^2)
    def longestPalindrome(self, s: str) -> str:

        def palind(s, l, r): 
            while 0 <= l and r < len(s) and s[l] == s[r]: 
                l -=1 
                r += 1 

            return s[l+1:r]   # 1 word for odd, 2 words for even  

        res = "" 

        for i in range(len(s)): 
            odd = palind(s, i, i) 
            even = palind(s, i, i+1) 

            s1 = palind(s, i, i)
            if len(s1) > len(res): res = s1
            
            s2 = palind(s, i, i+1)
            if len(s2) > len(res): res = s2

        return res              


    
   # starting at l,r expand outwards to find the biggest palindrome
   #      <--   --> 
                        
            class Solution:     # T:(N^2)
    def countSubstrings(self, s: str) -> int:
        def palind(L,R):
            output =0
            while L >= 0 and R < len(s) and s[L] == s[R]:
                output += 1
                L -= 1
                R += 1
            return output 

        count = 0 

        for i in range(len(s)):
            count += palind(i,i)
            count += palind(i,i+1)
        return count         


class Solution:   # 12131 T:O(1)
    def numDecodings(self, s: str) -> int:

        dp = [0] * (len(s)+1)
        dp[0] = 1 

        for i in range(1, len(dp)):

            if s[i-1] != '0': 
                dp[i] = dp[i-1]                            

            if i > 1 and '10' <= s[i-2 : i] <= '26':     # check the 2-digits 
                dp[i] += dp[i-2] 
            print(dp, "s", s[i-1])
                          
        return dp[-1]                     # dp: like [1, 1, 2, 3, 5, 5]

# [1, 1, 0, 0, 0, 0] s 1



# T: O(amount * len(coins)) 
# S: O(amount) 
# coins = [1,2,5], amount = 6
#       0, 1, 2, 3, 4, 5, 6  
#  dP: [0, 1, 1, 2, 2, 1, 2]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        dp = [0] + [float("inf")] * amount 
        
        for coin in coins: 
            for i in range(coin, amount+1): 
                dp[i] = min(dp[i], dp[i-coin]+ 1)

                

        return dp[amount] if dp[amount] != float("inf") else -1         

        # dp = [float("inf") for _ in range(amount+1)]
        
        
      class Solution:     # O(n)/O(1) : Time/Memory nums = [2,3,-2,4] Output: 6
    def maxProduct(self, nums: List[int]) -> int:
        
        res = nums[0] 
        curMax, curMin = 1, 1
        
        for n in nums: 

            tmp = n * curMax 

            curMax = max(tmp, curMin * n, n)
            curMin = min(tmp, curMin * n, n) 

            res = max(res, curMax)

        return res     
 
        # we prepare curMax and curMin cases just in case two neg like -4 * -4 happens 
  
  
 # s = "leetcode" wordDict = ["leet","code"]
# [True, False, False, False, True, False, False, False, True]
# T: O(n^2*m)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        dp = [True] + [False] * len(s) 

        for i in range(1, len(s)+1): 
            for word in wordDict: 
                if dp[i - len(word)] and s[i - len(word) : i] == word: 
                    dp[i] = True 

        return dp[-1]            

               
        
        

    #                              dp
    #       l     e     e       t      c     o       d     e    
        # [True, False, False, False, True, False, False, False,  True]
        #   0       1    2       3     4     5      6       7      8     

        
        
        
        class Solution:     # nums = [1, 2, 3, 4, 5] 
    def lengthOfLIS(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp) 

        


        # dp:    [1, 2, 1, 3, 3, 4]
        # nums = [0, 1, 0, 3, 2, 3]
        # only increment when nums[i] is larger 

        # 1 0 [1, 2, 1, 1, 1, 1]
        # 3 0 [1, 2, 1, 2, 1, 1]
        # 3 1 [1, 2, 1, 3, 1, 1]
        # 3 2 [1, 2, 1, 3, 1, 1]
        # 4 0 [1, 2, 1, 3, 2, 1]
        # 4 1 [1, 2, 1, 3, 3, 1]
        # 4 2 [1, 2, 1, 3, 3, 1]
        # 5 0 [1, 2, 1, 3, 3, 2]
        # 5 1 [1, 2, 1, 3, 3, 3]
        # 5 2 [1, 2, 1, 3, 3, 3]
        # 5 4 [1, 2, 1, 3, 3, 4]

        # if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], 1 + dp[j])

        # when nums[i] > nums[j] = 4 > 3            
        # dp[4] = max(dp[4], OR 1 + dp[3])
        # ,which dp[3] is the previous valu and just add "1"






        
        
  
  
   class Solution:     # nums = [1,5,11,5]
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False

        dp = set()
        dp.add(0)
        target = sum(nums) // 2

        for i in range(len(nums)-1):
            store = set()
            
            for t in dp:
                store.add(t + nums[i])
                store.add(t)

            dp = store
        return True if target in dp else False    



      
      
      
      
      
      
        
        
      
      
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


