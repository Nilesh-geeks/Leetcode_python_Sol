Question :: 2540. Minimum Common Value

Given two integer arrays nums1 and nums2, sorted in non-decreasing order, return the minimum integer common to both arrays. If there is no common integer amongst nums1 and nums2, return -1.

Note that an integer is said to be common to nums1 and nums2 if both arrays have at least one occurrence of that integer.

 
Solution::

Complexity::

Time complexity:
O(N) 

Space complexity:
O(N)

Code::
class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=0 
        j=0 
        while i<len(nums1) and j<len(nums2):
            if(nums1[i] == nums2[j]):
                return nums1[i]
            if(nums1[i] > nums2[j]):
                j+=1
            else:
                i+=1
        return -1

        