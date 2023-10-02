class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        # 1. one player's removal does not affect the other player's next steps
        # 2. Who's winning the game just depend on Triple A > Tripe B

        # The collections.Counter() is used to count the occurrences of characters in the string.
        # The groupby(colors) function groups consecutive characters in the string.
        # actually slower than first version


        c = collections.Counter()
        for x, t in groupby(colors):
            c[x] += max(len(list(t))-2, 0)
            
        return c['A'] > c['B'
