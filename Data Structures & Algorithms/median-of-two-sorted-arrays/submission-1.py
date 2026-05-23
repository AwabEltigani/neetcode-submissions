class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        a,b = nums1,nums2

        if len(a) > len(b):
            a,b = b,a
        
        total = len(a) + len(b)
        half = (total + 1) // 2
        LeftA = 0
        RightA = len(a) - 1

        while True:
            leftPartitionA = (LeftA + RightA) // 2 if (LeftA <= RightA) else -1
            leftPartitionB = half - (leftPartitionA + 1) - 1

            leftValueA = a[leftPartitionA] if leftPartitionA >= 0 else float("-infinity")
            rightValueA = a[leftPartitionA + 1] if (leftPartitionA + 1) < len(a) else float("infinity")
            leftValueB = b[leftPartitionB] if leftPartitionB >= 0 else float("-infinity")
            rightValueB = b[leftPartitionB + 1] if (leftPartitionB + 1) < len(b) else float("infinity")

            if leftValueA <= rightValueB and leftValueB <= rightValueA:
                if total % 2 != 0:
                    return float(max(leftValueA, leftValueB))
                else:
                    return (max(leftValueA, leftValueB) + min(rightValueA, rightValueB)) / 2.0
            elif leftValueA > rightValueB:
                RightA = leftPartitionA - 1
            else:
                LeftA = leftPartitionA + 1