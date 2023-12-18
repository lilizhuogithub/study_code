from typing import List
# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for i in range(9):
#             if len(set(board[i])) != len(list(board[i])):
#                 return False
#             if len(list(board[j][i] for j in range(9))) != len(set(board[j][i] for j in range(9))):
#                 return False
#         for i in range(3):
#             for j in range(3):
#                 if len(set(board[3*i+k][3*j+l] for k in range(3) for l in range(3))) != len(list(board[3*i+k][3*j+l] for k in range(3) for l in range(3))):
#                     return False
#         return True

# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         for i in range(9):
#             row_count = {}   # 用字典记录每行每列每个九宫格中数字出现的次数
#             col_count = {}   
#             box_count = {}

#             for j in range(9):
#                 # 检查行
#                 if board[i][j] != '.':
#                     count = row_count.get(board[i][j])	# 获取键为i的值，由以下代码可知第一次出现count==1。
#                     count = count+1 if count is not None else 1
#                     row_count[board[i][j]] = count               
#                     # row_count[board[i][j]] += 1
	
#                     if row_count[board[i][j]] > 1:
#                         return False

#                 # 检查列
#                 if board[j][i] != '.':
#                     # col_count[board[j][i]] += 1
#                     count = col_count.get(board[j][i])	# 获取键为i的值，由以下代码可知第一次出现count==1。
#                     count = count+1 if count is not None else 1
#                     col_count[board[j][i]] = count
#                     if col_count[board[j][i]] > 1:
#                         return False

#                 # 计算九宫格的索引
#                 box_row = 3 * (i // 3) + j // 3
#                 box_col = 3 * (i % 3) + j % 3

#                 # 检查九宫格
#                 if board[box_row][box_col] != '.':
#                     # box_count[board[box_row][box_col]] += 1
#                     count = box_count.get(board[box_row][box_col])	# 获取键为i的值，由以下代码可知第一次出现count==1。
#                     count = count+1 if count is not None else 1
#                     box_count[board[box_row][box_col]] = count
#                     if box_count[board[box_row][box_col]] > 1:
#                         return False
#         return True

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_count = {str(num): 0 for num in range(1, 10)}
            col_count = {str(num): 0 for num in range(1, 10)}
            box_count = {str(num): 0 for num in range(1, 10)}

            for j in range(9):
                # 检查行
                if board[i][j] != '.':
                    row_count[board[i][j]] += 1
                    if row_count[board[i][j]] > 1:
                        return False

                # 检查列
                if board[j][i] != '.':
                    col_count[board[j][i]] += 1
                    if col_count[board[j][i]] > 1:
                        return False

                # 计算九宫格的索引
                box_row = 3 * (i // 3) + j // 3
                box_col = 3 * (i % 3) + j % 3

                # 检查九宫格
                if board[box_row][box_col] != '.':
                    box_count[board[box_row][box_col]] += 1
                    if box_count[board[box_row][box_col]] > 1:
                        return False

        return True

# 测试
s = Solution()
print(s.isValidSudoku([["5","3",".",".","7",".",".",".","."],
                       ["6",".",".","1","9","5",".",".","."],
                       [".","9","8",".",".",".",".","6","."],
                       ["8",".",".",".","6",".",".",".","3"],
                       ["4",".",".","8",".","3",".",".","1"],
                       ["7",".",".",".","2",".",".",".","6"],
                       [".","6",".",".",".",".","2","8","."],
                       [".",".",".","4","1","9",".",".","5"],
                       [".",".",".",".","8",".",".","7","9"]]))
# False
print(s.isValidSudoku([["8","3",".",".","7",".",".",".","."],
                       ["6",".",".","1","9","5",".",".","."],
                       [".","9","8",".",".",".",".","6","."],
                       ["8",".",".",".","6",".",".",".","3"],
                       ["4",".",".","8",".","3",".",".","1"],
                       ["7",".",".",".","2",".",".",".","6"],
                       [".","6",".",".",".",".","2","8","."],
                       [".",".",".","4","1","9",".",".","5"],
                       [".",".",".",".","8",".",".","7","9"]]))



