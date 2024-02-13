Question :: 2108. Find First Palindromic String in the Array

Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.
Solution::

Complexity
Time complexity:
O(N*s) , s = length of max string
Space complexity:
O(1)
Code
   class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            if self.palindrome(s)==1:
                return s
        return ""
    def palindrome(self , str)->bool:
        i=0 
        j=len(str)-1
        while(i<=j):
            if(str[i]!=str[j]):
                return False
            i+=1
            j-=1
        return True