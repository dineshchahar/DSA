# given unsorted
"""Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.

You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space."""
# this is cyclic sort.

# we store the values in the given array (we the solution lies in the range [1,n+1], where n is the range of array.)

# using the cyclic sort we find the puts the number in the correct position (only if the number in in range [1,n], skips all other.)

# we again iterate over the array and find the element where nums[i]! = i+1 , if no found it should return n+1
# why this is o(n) - 
"""So across the whole algorithm:

Each index can be “fixed” at most once

Total number of swaps is ≤ n

The pointer i moves from 0 to n-1"""
class Solution:
    def firstMissingPositive(nums):
        n = len(nums)
        i =0 
        while i < n:
            x = nums[i]
            crt = x-1
            if 1<=x<=n and nums[crt] != x:
                nums[i],nums[crt] = nums[crt],nums[i]
            else:
                i+=1
        for i in range(n):
            if nums[i]!= i+1:
                return i+1
        return n+1
    
