Question :: 1481. Least Number of Unique Integers after K Removals
Given an array of integers arr and an integer k. Find the least number of unique integers after removing exactly k elements.
 
Solution::

Complexity::

Time complexity:
O(N) 

Space complexity:
O(N)

Code::
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        m = collections.Counter(arr)
        v = list(m.values())
        v.sort()
        cnt =0
        for i in range(len(v)):

            if k > v[i]:
                k -= v[i]
                v[i] = 0
            else:
                v[i] -= k
                k = 0
            if v[i] != 0:
                cnt += 1
        return cnt




        