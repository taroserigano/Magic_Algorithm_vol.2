class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1

        while l <= r: 
            m = (l + r) // 2 

            if nums[m] == target:
                return m 
            elif nums[m] < target:
                l = m + 1 
            elif nums[m] > target:
                r = m -1 
        return -1     
                     

        
    
    # set up l and r 
    # while l to r, define m, move l and r 



class Solution:             # O(log nm)
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        cols, rows = len(matrix[0]), len(matrix) 
        l, r = 0, cols*rows-1 

        while l <= r: 
            m = (l+r) // 2 

            search =  matrix[m // cols][m % cols]

            if search == target:
                return True 

            elif search < target:
                l = m + 1 
            elif search > target:
                r = m - 1 
        return False             



              
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 0 

        while l <= r: 
            m = (l + r) // 2 
            total = 0 

            for p in piles:
                total += math.ceil(p / m) 

            if total <= h:
                res = m 
                r = m - 1
            else: 
                l = m + 1 
            
        return res         



            




                         


# binary search from 0 to max(piles)
# divide every pile and count total time
# keep aiming for minimum number 


    
    # set l to r (max) 
    # go through every value 1, 2, 3 ..... max to find minimum eat amount per hour that can eat all piles
    # examine by pile / eat per hour 
    # if total time less than h, this is valid 
        
        
    
# nums = [4,5,6,7,0,1,2], target = 0
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0 
        R = len(nums) -1 

        while L <= R: 

            m = (L+R) // 2 

            if nums[m] == target:
                return m 
            
            if nums[L] <= nums[m]:                    # L            R
                if nums[L] <= target <= nums[m]:     # [     T      ]
                    R = m - 1                        # [456  7   012]       
                else:                                #    T               target is here     
                    L = m + 1                        #           T        target is here 

            elif nums[m] <= nums[R]:
                if nums[m] <= target <= nums[R]: 
                    L = m + 1
                else:
                    R = m - 1
        return -1                 





    
    #   CASE 1 
    # [ 4, 5, 6, 7, 0, 1, 2]
    #   L        M        R      [T]arget = 0 
    #       T         
  # 1.  L    <=     T     <= M 
   #    [ search   ]


    #   CASE 2 
    # [ 4, 5, 6, 7, 0, 1, 2]
    #   L        M        R      [T]arget = 0 
    #               T 
  # 1.  M   <=     T     <= R 
   #              [ search   ]
    
    
    
    
    
    
    
    
    
class Solution:
    def findMin(self, nums: List[int]) -> int:
              
        l, r = 0, len(nums)-1 
        
        while l < r: 
            m = (l+r) // 2 
            
            if nums[m] > nums[r]:
                l = m + 1                            # find possibly smaller value in LEFT 
                                                     # [3, 4, 5, 1, 2 ] <-- 
            elif nums[m] < nums[r]:                  #        T 
                r = m                  # move R to the middle      L  M <---  R       L  R  
        return nums[l]                 #                           1, 2,  3,  4       1, 2, 3, 4, 
    
    
    # [3,4,5,1,2]
    #  L   M   R
    #  M:5 > R:2   =   L = M + 1  
    #  [1,  2]
    #  L,M  R
    #  M:1  < R:2 => R = M:1 
    # L < R x break, return nums[L] == 1 
        
        
        
        
        
        
        
        
        
        
        class TimeMap:
    
    def __init__(self):
        self.map = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.map:
            self.map[key] = [] 

        self.map[key].append([value, timestamp])    
        
    def get(self, key: str, timestamp: int) -> str:

        res = ""
        values = self.map.get(key, [])
        left, right = 0, len(values)-1

        while left <= right: 
            m = (left + right) // 2

            if values[m][1] <= timestamp: 
                res = values[m][0]
                left = m + 1 
            else:
                right = m - 1
        return res             







        # O(p log p) 
        # res = "" 
        # values = self.dict.get(key, [])

        # l, r = 0, len(values)-1

        # while l <= r: 
        #     m = (l + r) // 2 
        #     if values[m][1] <= timestamp: 
        #         res = values[m][0]
        #         l = m + 1 
        #     else:
        #         r = m-1 
        # return res              



            
        
        
        
        
        
#         while l <= r:
#             mid = (l+r)//2
#             if values[mid][1] == timestamp: return values[mid][0]
#             elif values[mid][1] < timestamp:
#                 l = mid+1
#             else:
#                 r = mid-1
                
#         return values[r][0] if r >= 0 else ""

#     def __init__(self):
#         self.store = {} # [val, timestamp] 
        
#     def set(self, key: str, value: str, timestamp: int) -> None:
#         if key not in self.store: 
#             self.store[key] = [] 
        
#         self.store[key].append([value, timestamp])
            

#     def get(self, key: str, timestamp: int) -> str:
#         res = "" 
#         values = self.store.get(key, []) # if no result, it returns empty[] 
        
#         l, r = 0, len(values) -1 
        
#         while l <= r: 
#             m = (l + r) // 2
#             # values[middle] and [0=value][1=timestamp]
#             if values[m][1] <= timestamp: # if timestamp less or equal, this is good enough already so just store it for now
#                 res = values[m][0]
#                 l = m +1 
#             else: 
#                 r = m -1 
#         return res        
            

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

# O(log min(n+m))   
# nums1 = [1,3], nums2 = [2] 
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(B) < len(A):
            A, B = B, A

        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2  # A
            j = half - i - 2  # B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # odd
                if total % 2:
                    return min(Aright, Bright)
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
    


        
        

# get the A Right portion [i] (maximum) 
# and get the B Left portion [j] (minimum)
# and divide by //2, is the median 
# if odd, then minimum of(A right and B right) is the median 

# A, B = nums1, nums2   
#         if len(B) < len(A):      # A needs to be shorter 
#             A, B = B, A

#         total = len(nums1) + len(nums2)
#         half = total // 2

#         l, r = 0, len(A) - 1

#         while True:  # separater 
#             i = (l + r) // 2  # A
#             j = half - i - 2  # B   for array index starts from 0, -1 (A) and -1 (B), half is not 0 indexed  
            
#             # like if A = [1], only one num, then A[i+1] case needs to be covered 
#             # if out of bounce, make it "inf"
#             Aleft = A[i] if i >= 0 else float("-infinity")
#             Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
#             Bleft = B[j] if j >= 0 else float("-infinity")
#             Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

#             # if partition is correct
#             if Aleft <= Bright and Bleft <= Aright:
#                 # odd
#                 if total % 2:
#                     return min(Aright, Bright)
#                 # even
#                 return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

#             elif Aleft < Bright:
#                 l = i + 1
#             else: # Aleft > Bright 
#                 r = i - 1 









        
        
        
