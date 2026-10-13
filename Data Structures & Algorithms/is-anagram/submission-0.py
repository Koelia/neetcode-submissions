class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):        #both strings need to have the same length
            return False

        countS, countT = {}, {}     #creating the hashmap

        for i in range(len(s)):     #we know t and s have the same length
            countS[s[i]] = 1 + countS.get(s[i],0)  #filling out the hashmap
            countT[t[i]] = 1 + countT.get(t[i],0)
        
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False

        return True