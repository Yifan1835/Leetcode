class Solution:
    def minDeletions(self, s: str) -> int:

        #TC: O(len(s))
        #SC: O(max(freq(len(s))))
        #Just decrease characters with repetiting frequency to a frequency that is never seen
        
        cnt = collections.Counter(s)
        seen = set()
        res = 0

        for _, i in cnt.items():
            while i > 0 and i in seen:
                res += 1
                i -= 1
            seen.add(i)
        return res
