class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        # 1. one player's removal does not affect the other player's next steps
        # 2. Who's winning the game just depend on Triple A > Tripe B
        # Time: O(n)
        # Space: O(1)

        b_score = 0
        a_score = 0

        # deal with edge case using for loop
        for i in range(1, len(colors)-1):
            if colors[i-1] == 'A' and colors[i] == 'A' and colors[i+1] == 'A':
                a_score += 1
            if colors[i-1] == 'B' and colors[i] == 'B' and colors[i+1] == 'B':
                b_score += 1
        
        return a_score > b_score
