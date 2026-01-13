# find all the anagrams. given two string s and t , 
from collections import Counter
class solution:
    def findAnagrams(self,s,t):
        n ,m = len(s),len(t)
        if m>n:
            return []
        need = Counter(t)
        missing = m
        left = 0

        ans = []
        for right,ch in enumerate(s):
            if need[ch] > 0:
                missing -=1

            need[ch]-=1

            while right-left + 1 > m:
                left_ch = s[left]
                if need[left_ch] >=0:
                    missing +=1
                need[left_ch] +=1
                left +=1
            if right - left + 1 == m and missing == 0:
                ans.append(left)
        return ans




s = "abab"
t = "ab"
sol = solution().findAnagrams(s,t)

            
print(sol)



