# valid SudoKu board

class solution:
    def isValidSudoku(self, board):
        r = [set() for _ in range(9)]
        c = [set() for _ in range(9)]
        b = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                ele = board[i][j]
                if ele == "." or " ":
                    continue
                box_idx = (i//3)*3 + j//3
                if ele in r[i] or ele in c[j] or ele in b[box_idx]:
                    return False
                r[i].add(ele)
                c[j].add(ele)
                b[box_idx].add(ele)
        return True