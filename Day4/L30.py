"""
Docstring for Day4.L30

You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.
"""
from collections import Counter
# instead of going through every index, we can jump by word length (just like sliding window with fixed size chunks) and also need to check for all offsets within a word length
class Solution:
    def findSubstring(self,s,words):
        n = len(s)
        m = len(words)
        t = len(words[0])
        need = Counter(words)
        offset = 0
        ans = []
        for i in range(t):
            d = need.copy()
            missing = m
            start = i
            for end in range(offset,n-t+1,t):
                y = s[end:end+t]
                if y not in d or d[y] ==0:
                    d = need.copy()
                    missing = m
                    start = end+t
                    continue
                missing -=1
                d[y] -=1
                while end-start + t > m*t:
                    x = s[start:start+t] 
                    d[x]+=1
                    if d[x]>0:
                        missing +=1
                
                    start += t

                if missing ==0:
                    ans.append(start)
        return ans




                

            

    # def findSu

# failed approach
# class Solution:
#     def findSubstring(self,s,words):
#         n = len(s)
#         m = len(words)
#         t = len(words[0])
#         ans = []
#         if m*t > n:
#             return ans
#         need = Counter(words)
#         missing = m
#         end = 0
#         start = 0
#         while end < n-m:
#             x = s[end:end+m]
#             if x not in need and need[x] >0:
#                 end +=1
#             else:
#                 need[x] +=1
#                 missing -=1

#             while end + m - start >  m*t:
#                 y = s[start : start + t]
#                 if y not in need:
#                     start +=1
#                 else:
#                     missing +=1
#                     need[y] +=1
#             if missing ==0 and end + m - start == m*t:
#                 ans.append(start)  
#             end +=1
#         return ans


            
                
            

            

