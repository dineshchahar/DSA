# given the secret and guess return the number of digits that are in correct place and correct order and number of digits that are available in guess not in current position.
from collections import defaultdict
class Solution:
    def getHint(self,secret, guess):
        d = defaultdict(int)
        correct = 0
        abutnc = 0
        for idx,ch in enumerate(secret):
            if guess[idx] == ch:
                correct+=1
            else:
                d[ch] = d.get(ch,0) +1
        for idx, ch in enumerate(guess):
            if secret[idx] == ch:
                continue
            else:
                if ch in d and (d[ch]>0):
                    abutnc +=1
                    d[ch] -=1
    

        return f"{correct}A{abutnc}B"



        