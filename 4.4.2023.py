class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        numSet = set() 

        for n in nums: 
            if n in numSet:
                return True 
            numSet.add(n) 
        return False        


        numSet = set()

        for n in nums:
            if n in numSet:
                return True 
            numSet.add(n)
        return False     
        

        
        class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # return Counter(s) == Counter(t)

        # return ("").join(sorted(s)) == ("").join(sorted(t))

        if len(t) != len(s) : 
            return False 
        sMap = {} 
        tMap = {} 

        for i in range(len(s)): 
            sMap[s[i]] = sMap.get(s[i], 0) + 1 
            tMap[t[i]] = tMap.get(t[i], 0) + 1

        return sMap ==tMap 
             

        # sMap = {} 
        # tMap = {} 

        # for i in range(s): 
        #     sMap[s[i]] = sMap.get(s[i], 0) + 1 
        #     tMap[t[i]] = tMap.get(t[i], 0) + 1

        # return sMap.values() ==tMap.values()     

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        res = [] 

        for i in range(2): 
            for n in nums: 
                res.append(n) 

        return res          

  class Solution:   # arr = [17,18,5,4,6,1]
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightMax = -1 

        for i in range(len(arr)-1, -1, -1): 

            arr[i], rightMax = rightMax, max(arr[i], rightMax) 

        return arr         
                
class Solution:         # T: O(N). S: O(1). - s = "abc", t = "ahbgdc"
    def isSubsequence(self, s: str, t: str) -> bool:

        if not s: return True 


        i = 0 

        for target in t: 
            if s[i] == target: 
                i += 1 

                if i == len(s): return True 

        return False    


class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = s.strip().split()
        return len(s[-1])


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        map = {} 

        for i, n in enumerate(nums): 
            diff = target - n 

            if diff in map: 
                return [i, map[diff]] 

            map[n] = i 

        return map         

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
  

        res = "" 

        for char in zip(*strs): 
            if len(set(char)) == 1:
                res += char[0] 
            else:
                return res 
        return res             

    




# print c like this: 
#  ('f', 'f', 'f')
# ('l', 'l', 'l')
# ('o', 'o', 'i')
# ('w', 'w', 'g')


        # n = min(strs,key=len)
        # res = ""
        # for i in range(len(n)):
        #     for char in strs:
        #         if char[i] != strs[0][i]:
        #             return res
        #     res += strs[0][i]
        # return res
                
    
 class Solution:   # strs = # ["eat","tea","tan","ate","nat","bat"] 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map = {} 

        for s in strs: 
            sortedStr = "".join(sorted(s)) 

            print(sortedStr)

            if sortedStr in map:
                map[sortedStr].append(s) 
            else:
                map[sortedStr] = [s] 

        return map.values()              




        
# map: {  'aet': ['eat', 'tea', 'ate'], 
        # 'ant': ['tan', 'nat'], 
        # 'abt': ['bat']}

# sorted strings:
# aet
# aet
# ant
# aet
# ant
# abt




        # res = defaultdict(list)

        # for s in strs:
        #     res[tuple(sorted(s))].append(s)

        # return res.values()    
        

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0 

        for i in range(len(nums)): 

            if nums[i] != val: 
                nums[j] = nums[i] 
                j += 1 
        return j         


class Solution:emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    def numUniqueEmails(self, emails: List[str]) -> int:

        unique = set() 

        for e in emails: 
            local, domain = e.split("@")     # test.email+alex leetcode.com
            local = local.split("+")[0]      # test.email 
            local = local.replace(".", "")    
            unique.add((local, domain)) 

        return len(unique) 



class Solution:      # s = "foo", t = "bar"
    def isIsomorphic(self, s: str, t: str) -> bool:

        # print(set(zip(s, t)))   - {('e', 'a'), ('g', 'd')}
        
        # return len(set(zip(s, t))) == len(set(s)) == len(set(t))

        map = {} 

        for i in range(len(s)): 

            if s[i] not in map: 
                map[s[i]] = t[i] 

            elif map[s[i]] != t[i]: 
                return False 

        return len(set(map.values() )) == len(map.values())          

             


        # map = {} 

        # for i in range(len(s)): 

        #     if s[i] not in map: 
        #         map[s[i]] = t[i] 
        #     elif map[s[i]] != t[i]:
        #         return False 

        # return len(set(map.values() ) ) == len(map.values()) # check dupe                






# 1. store the char that replace
# 2. if repeated, and not working, Fail         
        
class Solution:
    def majorityElement(self, nums):


        nums.sort()
        print(nums)
        return nums[len(nums)//2]


class Solution:     # nums1 = [4,1,2], nums2 = [1,3,4,2]
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [] 

        for num1 in nums1: 
            found = False 

            for num2 in nums2[nums2.index(num1):]: 

                if num2 > num1: 
                    found = True 
                    res.append(num2) 
                    break 
            if not found:
                res.append(-1) 

        return res                 







        res = [] 

        for num1 in nums1: 
            found = False 

            for num2 in nums2[nums2.index(num1):]:

                if num2 > num1: 
                    found = True 
                    res.append(num2) 
                    break 

            if not found: 
                res.append(-1) 

        return res                               


        res = [] 

        for num1 in nums1: 
            found = False 

            for num2 in nums2[nums2.index(num1):]: 

                if num2 > num1: 
                    res.append(num2) 
                    found = True 
                    break 
            if not found: 
                res.append(-1)

        return res         
        

class Solution:     # O(n) 
    def pivotIndex(self, nums: List[int]) -> int:



        for i, n in enumerate(nums): 

            rightSum = total - leftSum - n 

            if rightSum == leftSum: 
                return i 

            leftSum += n 

        return -1 







        total = sum(nums) 
        leftSum = 0 

        for i, n in enumerate(nums): 

            rightSum = total - leftSum - n
            if rightSum == leftSum: 
                return i 

            leftSum += n 

        return -1          


class NumArray:

    def __init__(self, nums: List[int]):
        

    def sumRange(self, left: int, right: int) -> int:
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

class Solution:    # T: O(N), S: O(N) 
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:  

        map = {} 
        res = [] 

        for n in nums:

            map[n] = map.get(n, 0)+1 

        for i in range(1, len(nums)+1):

            if i not in map: 
                res.append(i) 
        return res             

        
class Solution:          # T&S: O(N)   text = "nlaebolko"  
    def maxNumberOfBalloons(self, text: str) -> int:
        countText = Counter(text) 
        countBal = Counter("balloon")

        res = float("inf") 

        for c in countBal: 
            res = min(res, countText[c] // countBal[c]) 

        return res     










# b 1 1
# a 1 1
# l 2 2
# o 2 1
# n 1 1

class Solution:   # A's char matches B's word ?  
    def wordPattern(self, pattern: str, s: str) -> bool:

        map = {} 

        words = s.split(" ")
        if len(pattern)!=len(words) or len(set(pattern)) != len(set(words)): return False 

        for p, w in zip(pattern, words): 
                if p not in map: 
                        map[p] = w 
                elif map[p] != w:
                        return False 

        return True                         


class MyHashMap:

    def __init__(self):
        

    def put(self, key: int, value: int) -> None:
        

    def get(self, key: int) -> int:
        

    def remove(self, key: int) -> None:
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

   
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = [] 

        count = Counter(nums) 

        for num, count in count.items(): 
            heappush(res, (count, num)) 

            if len(res) >k:
                heappop(res) 

        return [num for count, num in res]
        

class Solution:   # nums = [1,2,3,4]
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        pre = 1 
        pos = 1
        res = [1] * len(nums)

        for i in range(len(nums)):
            res[i] *= pre 
            pre *= nums[i] 

        for i in  range(len(nums)-1,-1,-1):
            res[i] *= pos 
            pos *= nums[i]    

        return res     
     




# [1, 1, 1, 1]
# 1
# [1, 1, 1, 1]
# 2
# [1, 1, 2, 1]
# 6
# [1, 1, 2, 6]
# 24
# [1, 1, 2, 6]
# 4
# [1, 1, 8, 6]
# 12
# [1, 12, 8, 6]
# 24
# [24, 12, 8, 6]
# 24






        # res = [1] * (len(nums)) 

        # prefix = 1 
        # for i in range(len(nums)):
        #     res[i] *= prefix        # 1, 1, 2, 6 
        #     prefix *= nums[i]       # 1, 1, 2, 6  

        # postfix = 1 
        # for i in range(len(nums)-1, -1, -1):
        #     res[i] *= postfix       # <- 24, 12, 8, 6 
        #     postfix *= nums[i]      # -> 1,  4, 12, 24,

        # return res         

# 1. set up res [1] for len 
# 2. prefix = 1 , for loop for each 
# 3. * res and nums[i] 

# 4. do the same for each backwards 

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = defaultdict(set) 
        cols = defaultdict(set) 
        sq = defaultdict(set) 

        for r in range(9): 
            for c in range(9): 

                if board[r][c] == ".":
                    continue

                if (board[r][c] in rows[r] or 
                board[r][c] in cols[c] or 
                board[r][c] in sq[(r//3, c//3)]): 
                    return False 

                rows[r].add(board[r][c]) 
                cols[c].add(board[r][c]) 
                sq[(r//3,c//3)].add(board[r][c]) 

        return True             



          




# sq: (0,0), (0, 1), (0, 2)

# print(cols) defaultdict(<class 'set'>, {0: {'8', '4', '6', '5', '7'}, 1: {'9', '6', '3'}, 4: {'8', '1', '6', '2', '9', '7'}, 3: {'1', '8', '4'}, 5: {'9', '5', '3'}, 2: {'8'}, 7: {'8', '6', '7'}, 8: {'3', '1', '6', '9', '5'}, 6: {'2'}})





    



        # set up cols, rows, squares 
        # 1. for loop 9 and 9 
        # 2. check "." case
        # 3. check cols, rows and squares 

        # cols = defaultdict(set)
        # rows = defaultdict(set) 
        # squares = defaultdict(set)

        # for r in range(9):
        #     for c in range(9): 
        #         if board[r][c] == ".": 
        #             continue 
        #         if (
        #             board[r][c] in rows[r]
        #             or board[r][c] in cols[c]
        #             or board[r][c] in squares[(r // 3, c // 3)]
        #         ):
        #             return False
        #         cols[c].add(board[r][c])
        #         rows[r].add(board[r][c])
        #         squares[(r // 3, c // 3)].add(board[r][c])

        # return True              


class Codec:
    def encode(self, strs: List[str]) -> str:
        res = "" 

        for s in strs:
            res += str(len(s)) + "/" + s  
        return res     
  

    def decode(self, s: str) -> List[str]:  # 5  #             Hello        5#World
                                            # L  R,R+1 --->   R+1+length 

        i = 0 
        res = [] 

        while i < len(s): 

            slash = s.find("/", i) 
            length = int(s[i : slash]) 
            print(s[i:slash])
            i = length + slash + 1 
            res.append(s[slash+1 : i])

        return res     
   






        # res = [] 
        # str = "" 
        # L = 0 

        # while L < len(s): 
        #     R = L 

        #     while s[R] != "#": R += 1 

        #     length = int(s[L: R])

        #     str = s[R+1 : R + length + 1] 

        #     res.append(str) 

        #     L = R + length + 1
        # return res     





# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

                    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums) 

        res = 0 

        for n in nums: 
            if (n-1) not in numSet: 
                count = 1 


                while (n+count) in numSet:
                    count+=1 

                res = max(res, count) 

        return res              

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        high = len(nums) - 1
        mid = 0

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid +=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums

 class Solution:     # O(n) 
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0 

        for i in range(1, len(prices)): 
            if prices[i] > prices[i - 1]: 
                profit += (prices[i] - prices[i - 1]) 

        return profit         


# Input: s = "cbaebabacd", p = "abc"
# Output: [0,6]

from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        start = 0 
        sMap, pMap = {}, {} 
        res = [] 

        for c in p:
            pMap[c] = pMap.get(c, 0) + 1 

        for i in range(len(s)):     
            sMap[s[i]] = 1 + sMap.get(s[i], 0) .

            if i >= len(p) - 1: 
                if sMap == pMap: 
                    res.append(start)

                if s[start] in sMap:         
                    sMap[s[start]] -= 1 
                    if sMap[s[start]] == 0: 
                        del sMap[s[start]] 

                start += 1 
        return res                 


   
# ans = []
#     count = collections.Counter(p)
#     required = len(p)

#     for r, c in enumerate(s):
#       count[c] -= 1
#       if count[c] >= 0:
#         required -= 1
#       if r >= len(p):
#         count[s[r - len(p)]] += 1
#         if count[s[r - len(p)]] > 0:
#           required += 1
#       if required == 0:
#         ans.append(r - len(p) + 1)

#     return ans
                      
        
# 1. keep storing as looping  
# 2. once reached the end of window, 
# 3. check and clean up 
  
                    
            
        
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        hay = len(haystack)
        need = len(needle) 

        for i in range(hay):

            print(needle[i:i+need])
            if haystack[i: i+need] == needle:
                return i 

        return -1         

class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        if(nums == null || nums.length == 0) return ""; 

        String[] strs = new String[nums.length]; 

        







        








     
      


        





      
        


        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        



    
      
      
        
        
        
        
        



        
        
        
        
        
        









