from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            # 终止条件
            if not 0 <= i < len(board) or not 0 <= j <len(board[0]) or board[i][j] != word[k]: return False
            if k == len(word) - 1: return True
            # 递推
            board[i][j] = ' '
            res = dfs(i + 1, j, k+1) or dfs(i - 1, j, k+1) or dfs(i, j + 1, k+1) or dfs(i, j - 1, k+1)
            board[i][j] = word[k]
            return res

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0): return True
        return False


c = Solution()
print(c.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))


