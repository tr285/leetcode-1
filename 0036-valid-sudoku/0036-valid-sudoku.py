class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        verify = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                  continue
                row_item = (r, val)
                col_item = (val,c)
                box_item = (r // 3,c//3, val)
                if row_item in verify or col_item in verify or box_item in verify:
                    return False

                verify.add(row_item)
                verify.add(col_item)
                verify.add(box_item)
        return True