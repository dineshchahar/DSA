"""Given an integer array nums and an integer k, return true if nums has a good subarray or false otherwise.

A good subarray is a subarray where:

its length is at least two, and
the sum of the elements of the subarray is a multiple of k.
Note that:

A subarray is a contiguous part of the array.
An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k."""

class Solution:
    def checkSubarraySum(self,arr,k):
        total = 0
        d = {0:-1}

        for i,ch in enumerate(arr):
            total +=ch
            remainder  = total % k
            if remainder not in d:
                d[remainder] =i
            elif remainder in d and (i-d[remainder]>1):
                return True
        return False