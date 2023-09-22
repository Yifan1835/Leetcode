class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # notice: "ace" is a subsequence of "abcde" while "aec" is not
        # solution: dump previous matched sequnce

        for c in s:
            i = t.find(c)
            if i==-1:
                return False
            else:
                t = t[i+1:]
        return True
