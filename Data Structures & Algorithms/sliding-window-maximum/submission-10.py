from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        """
        Data Structure -> Deque why because O(1) insertion to the front and rear
                                                 removal O(1) from front and rear
        O(n) time -> best case when the array is in increasing order O(n*k) time -> worst case when the array is in decreasing order
        O(n) space -> results arr

        Explaination:

        We start with finding the max in the 1st kth subarr then keep track of it 
        then there are 3 diffrent senarios if the number being added is greater than the current max then its = the max
        if the item is less than the max then we just add the num to the arr
        if the max is kicked off the rear of the arr then we check if the item being added is greater if it is then. we just have it as max
        but if not then we need to iterate thru the arr and figure out which one is the max (which is the worst case senario)

        Edge cases:
        ->if k == len(nums) ->itrate on the arr and return the max which is just an [n]

        """

        de = deque()
        curMax = -1

        if k == len(nums):
            for num in nums:
                if num > curMax:
                    curMax = num
            return [curMax]
        
        result = []

        for i in range(k):
            if nums[i] > curMax:
                curMax = nums[i]
            de.append(nums[i])
        
        result.append(curMax)
        

        

        for i in range(1,len(nums) - k + 1):

            itemLeft = de.popleft()
            de.append(nums[k + i - 1])

            if itemLeft == curMax:
                if nums[k + i - 1] > itemLeft:
                    curMax = nums[k + i - 1]
                else:
                    curMax = -1
                    for num in de:
                         if num > curMax:
                            curMax = num
            
            if nums[i + k - 1] > curMax:
                curMax = nums[i + k - 1]
            
           
            
            result.append(curMax)
         
          

        
        return result
            


            

























