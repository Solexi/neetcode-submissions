from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sCount = Counter(s)
        tCount = Counter(t)

        for i in sCount:
            if sCount[i] != tCount[i]:
                return False
        return True

        print(sCount)