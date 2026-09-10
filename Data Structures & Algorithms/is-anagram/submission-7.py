class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char = {}
        if len(s)!= len(t):
            return False
        for i in s:
            char[i]= char.get(i,0)+1
        for j in t:
            if j in char:
                char[j]-=1
            else:
                char[j]=char.get(j,0)+1
        for i in char.values():
            if i!=0:
                return False
        return True    
        