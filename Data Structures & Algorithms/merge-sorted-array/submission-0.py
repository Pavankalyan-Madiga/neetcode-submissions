class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i=0
        j=0
        result=[]
        
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                result.append(nums1[i])
                i+=1
            else:
                result.append(nums2[j])
                j+=1
        while i<m:
            result.append(nums1[i])
            i+=1
        while j<n:
            result.append(nums2[j])
            j+=1
        
        for k in range(m+n):
            nums1[k]=result[k]

        return nums1