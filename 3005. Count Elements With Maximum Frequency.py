Question :: 3005. Count Elements With Maximum Frequency

You are given an array nums consisting of positive integers.

Return the total frequencies of elements in nums such that those elements all have the maximum frequency.

The frequency of an element is the number of occurrences of that element in the array.
Solution::

Complexity::

Time complexity:
O(N) 

Space complexity:
O(N)

Code::
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counter = Counter(nums)
        max_frq = max(counter.values())
        return sum(frq for frq in counter.values() if frq == max_frq)
      
        



        