class Solution:
    def minDeletions(self, s: str) -> int:

        #TC: O(len(s))
        #SC: O(max(freq(len(s))))
        #Just decrease characters with repetiting frequency to a frequency that is never seen
        
        seen = set([])
        res = 0
        freq_table = {}

        for c in s:
            freq_table[c] = 1 + freq_table.get(c,0)

        for i in freq_table.values():
            if i not in seen:
                seen.add(i)
            else:
                while i > 0 and i in seen:
                    i -= 1
                    res += 1
                if i > 0:
                    seen.add(i)

        return res
