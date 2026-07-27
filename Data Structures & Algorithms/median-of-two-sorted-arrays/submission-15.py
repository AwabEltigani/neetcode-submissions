class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums2,nums1 = nums1,nums2
        
        if len(nums1) == 0:
            if len(nums2)%2 == 0:
                return (nums2[(len(nums2)//2) - 1] + nums2[(len(nums2)//2)])/2
            else:
                return nums2[(len(nums2)//2)]

        total = len(nums1) + len(nums2)
        half = total//2
        l = 0
        r = len(nums1)
        neg_inf = float('-inf')
        pos_inf = float('inf')


        while r >= l:
            leftPartition = (l + r)//2
            rightPartition = half - leftPartition 
            if leftPartition == 0:
                nums1L = neg_inf
                nums1R = nums1[0]
            elif leftPartition == len(nums1):
                nums1L = nums1[len(nums1) - 1]
                nums1R = pos_inf
            else:
                nums1L = nums1[leftPartition - 1]
                nums1R = nums1[leftPartition]
            
            if rightPartition <= 0:
                nums2L = neg_inf
                nums2R = nums2[0]
            elif rightPartition >= len(nums2):
                nums2L = nums2[len(nums2) - 1]
                nums2R = pos_inf
            else:
                nums2L = nums2[rightPartition - 1]
                nums2R = nums2[rightPartition]
            print(nums2L,nums2R)
            print(nums1L,nums1R)
            
            
            
            if nums1R >= nums2L and nums2R >= nums1L:
                if total % 2 == 0:
                    
                    return (min(nums2R,nums1R) + max(nums1L,nums2L))/2
                else:
                    return min(nums2R,nums1R)
            else:
                l = leftPartition + 1


            

            