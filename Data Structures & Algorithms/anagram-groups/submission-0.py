class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)   #python deafult list

        
        for s in strs:
            count = [0] * 26            # we know a->z characters

            for c in s:         
                count[ord(c)-ord('a')] += 1    #for current string for ex: cat
                                            # key - 1z 1c 1t, value "act", "cat"

            res[tuple(count)].append(s)         #res[tuple(count)].append(s) is giving the key
                                            #.append(s) is adding the string to the list, for ex: currently 
                                            # has [1,0,1,..1,0] -> ["act"], then add current string 
                                            #[1,0,1,..1,0] -> ["act", "cat"]

        return list(res.values())                                 