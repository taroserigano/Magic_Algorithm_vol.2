def __init__(self, k: int, nums: List[int]):
        self.k = k 
        self.minHeap = nums 

        heapq.heapify(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)

        while len(self.minHeap) > self.k: 
            heapq.heappop(self.minHeap)

        return self.minHeap[0]    
        
        
        
        
        
        class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        minHeap = [] 
        res = [] 

        for x, y in points: 
            dist = (x ** 2) + (y ** 2) 
            minHeap.append([dist, x, y])

        heapq.heapify(minHeap)

        while k > 0: 
            dist, x, y = heapq.heappop(minHeap)    
            res.append([x, y])
            k -= 1 

        return res     

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = [] 
        heapq.heapify(minHeap)      

        for n in nums:
            heapq.heappush(minHeap, n)

        while len(minHeap) > k: 
            heapq.heappop(minHeap)

        return heapq.heappop(minHeap) 
        
        
        
        
        class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        c = Counter(tasks)
        store = [] 
        res = 0 

        for num, count in c.items(): 
            heapq.heappush(store, [-count, num])

        while store: 
            temp = [] 
            i = 0 
            while i <= n: 
                res += 1 

                if store: 
                    count, num = heapq.heappop(store)
                    count += 1 
                    if count < 0: temp.append([count, num]) 
                i += 1 
                if not temp and not store: break 

            for count, num in temp:
                heapq.heappush(store, [count, num]) 

        return res                


class MedianFinder(object):

        1 2 5 10     15 16  90 100 
         [min]           [max]    
                
    def __init__(self):
        self.bot = []    # pop largest val 
        self.top = []    # pop smallest val 
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: None
        """
        heappush(self.bot, -num)     # add neg. 
        heappush(self.top, -heappop(self.bot))   # add pos.  
        
        if len(self.top) > len(self.bot): 
            heappush(self.bot, -heappop(self.top)) 
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.bot) != len(self.top): 
            return -self.bot[0]
        else: 
            return (self.top[0] - self.bot[0]) / 2 


        
        

        
        
        
