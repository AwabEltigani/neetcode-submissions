class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        a = nums1
        b = nums2

        if len(a) > len(b):
            a,b = b,a
        
        total = len(a) + len(b)

        aL = 0
        aR = len(a) - 1
        bL = 0
        bR = len(b) - 1

        while True:

            leftA = (aR + aL) // 2
            rightA = leftA + 1
            leftB = (total//2 - leftA - 2)
            rightB = leftB + 1

          

            leftPartA = a[leftA] if leftA >= 0 else float("-infinity")
            rightPartA = a[rightA]  if (rightA < len(a)) else float("infinity")
            leftPartB = b[leftB] if (leftB >= 0) else float("-infinity")
            rightPartB = b[rightB] if (rightB < len(b)) else float("infinity")
            
            if rightPartB >= leftPartA and rightPartA >= leftPartB:
                
                if total%2 == 0:
                    return float((max(leftPartA,leftPartB)+min(rightPartA,rightPartB))/2)
                else:
                    return float(min(rightPartA,rightPartB))
            elif leftPartB > rightPartA:
                aL = leftA + 1
            else:
                aR = leftA - 1
            



            
