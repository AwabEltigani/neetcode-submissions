class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2

        if len(a) > len(b):
            b,a = a,b
        
        total = len(a) + len(b)
        aL = 0
        aR = len(a) - 1
        bL = 0
        bR = len(b) - 1

        while True:

            leftPartA = (aL + aR)//2 
            rightPartA = leftPartA + 1 
            leftPartB = ((total + 1) // 2) - 2 - leftPartA  
            rightPartB = leftPartB + 1

            
            leftValueA = a[leftPartA] if leftPartA >= 0 else float("-infinity")
            rightValueA = a[rightPartA] if rightPartA < len(a) else float("infinity")
            leftValueB = b[leftPartB] if leftPartB >= 0 else float("-infinity")
            rightValueB = b[rightPartB] if rightPartB < len(b) else float("infinity")

            if rightValueB >= leftValueA and rightValueA >= leftValueB:
                if total % 2 == 0:
                    return float((max(leftValueA,leftValueB) + min(rightValueB,rightValueA)) / 2)
                else:
                    return float(max(leftValueA,leftValueB))
            elif leftValueA > rightValueB:
                aR = leftPartA - 1
            else:
                aL = leftPartA + 1

            