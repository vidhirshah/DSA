def exist(board, word):
    def search(pos,i):
        if i == len(word):
            return True
        if pos[0] >= len(board) or pos[0] < 0:
            return False
        if pos[1] >= len(board[0])  or pos[1] < 0:
            return False
        if board[pos[0]][pos[1]] == '!':
            return False
        c = board[pos[0]][pos[1]]
        board[pos[0]][pos[1]] = "!"
        l = pos[0]
        r = pos[1]
        if c == word[i]:
            ans =  (search([pos[0]+1,pos[1]],i+1) or 
                   search([pos[0]-1,pos[1]],i+1) or
                   search([pos[0],pos[1]+1],i+1) or 
                   search([pos[0],pos[1]-1],i+1))
        else:
            ans = False
        board[pos[0]][pos[1]] = c
        return ans
    for i in range(len(board)):
        for j in range(len(board[0])):
            print(board)
            if search([i,j],0):
                return True
    return False

board = [["a","b"]]
word = "ba"
print(exist(board,word))