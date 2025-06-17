class Solution {
    public boolean isValidSudoku(char[][] board)
    {
     Solution sol = new Solution();
     boolean validRow = sol.isValidRow(board);
     boolean validCol = sol.isValidColumn(board);   
     if (!validRow || !validCol) return false;        //0,0 / 0,3 / 0,6
     for(int i = 0; i<3; i++)                               //3,0 / 3,3 / 3,6
     {
        for(int j = 0; j<3; j++)
        {
         char[][] sub = sol.getSubBox(board, i*3, j*3);
         boolean isValidSub = sol.isValidSubBox(sub);
         if(!isValidSub)
         {
            return false;
         }
        }
     }
     return true;
    }


    public char[][] getSubBox(char[][] board, int startRow, int startCol)
    {
    char[][] sub = new char[3][3];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            sub[i][j] = board[startRow + i][startCol + j];
        }
    }
    return sub;
    }


    public boolean isValidSubBox(char[][] board)
    {
        Map<Character, Integer> seen = new HashMap<>();
        for(int i = 0; i < 3; i++)
        {
          for(int j = 0; j < 3; j++)
         {
            if (board[i][j] == '.') continue;
            seen.put(board[i][j], seen.getOrDefault(board[i][j], 0)+1);
            if (seen.get(board[i][j]) > 1) return false;
         }
        }
        return true;
    }


    public boolean isValidRow(char[][] board)
    {
        Map<Character, Integer> seen = new HashMap<>();
        for(int i = 0; i < 9; i++)
        {
          for(int j = 0; j < 9; j++)
         {
            if (board[i][j] == '.') continue;
            seen.put(board[i][j], seen.getOrDefault(board[i][j], 0)+1);
           if (seen.get(board[i][j]) > 1) return false;
         }
         seen.clear();
        }
        return true;
    }


    public boolean isValidColumn(char[][] board)
    {
        Map<Character, Integer> seen = new HashMap<>();
        for(int i = 0; i < 9; i++)
        {
          for(int j = 0; j < 9; j++)
         {
            if (board[j][i] == '.') continue;
            seen.put(board[j][i], seen.getOrDefault(board[j][i], 0)+1);
           if (seen.get(board[j][i]) > 1) return false;
         }
          seen.clear();

        }
        return true;
    }
}