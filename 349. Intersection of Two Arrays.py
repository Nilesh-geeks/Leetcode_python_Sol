Question :: 349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
 
 
Solution::

Complexity::

Time complexity:
O(N) 

Space complexity:
O(N)

Code::
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = {}
        for x in nums1:
            m[x] = m.get(x,0)+1
        res = []
        for x in nums2:
            if x in m:
                res.append(x)
                del(m[x])
        return res

        
        