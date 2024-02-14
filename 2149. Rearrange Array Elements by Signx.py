Question :: 2149. Rearrange Array Elements by Sign

You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 
Solution::

Complexity::

Time complexity:
O(N) 

Space complexity:
O(N)

Code::
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        pos = 0 
        neg = 1
        for i in nums:
            if i>0:
                ans[pos] = i
                pos+=2
            else:
                ans[neg] = i
                neg+=2
        return ans

        