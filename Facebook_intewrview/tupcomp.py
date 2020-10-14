x = ('a', 2)
y = ('a', 2)

print(x is y)

board = [[1, 2],
         [1, 4],
         [5, 1]]
word = 1
first = [(i, j) for j in range(len(board[0])) for i in range(len(board)) if
         board[i][j] == word]
print(first)
